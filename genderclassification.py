def gender_classification_main(video_path, frame_placeholder=None, log_placeholder=None):
    import cv2, time
    import numpy as np
    import mediapipe as mp
    from roboflow import Roboflow
    from groq import Groq

    # Initialize models
    rf = Roboflow(api_key="waM5IrbdSRqBjOLWJFmx")
    project = rf.workspace().project("gender-bkoji")
    model = project.version(1).model

    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_drawing = mp.solutions.drawing_utils

    groq_client = Groq(api_key="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")

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        try:
            result = model.predict(frame, confidence=40, overlap=70).json()
            predictions = result.get("predictions", [])
            male_count = sum(1 for pred in predictions if pred['class'] == 'male')
            female_count = sum(1 for pred in predictions if pred['class'] == 'female')

            for pred in predictions:
                x, y, w, h = int(pred['x']), int(pred['y']), int(pred['width']), int(pred['height'])
                label = pred['class']
                color = (0, 255, 0) if label == 'female' else (255, 0, 0)
                cv2.rectangle(frame, (x - w//2, y - h//2), (x + w//2, y + h//2), color, 2)
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        except Exception as e:
            print("Roboflow error:", e)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(rgb)
        hand_raise_detected = False

        if result.pose_landmarks:
            landmarks = result.pose_landmarks.landmark
            left_hand = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
            right_hand = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
            head = landmarks[mp_pose.PoseLandmark.NOSE]

            if left_hand.y < head.y or right_hand.y < head.y:
                hand_raise_detected = True
                cv2.putText(frame, "Hand Raised!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

            mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        prompt_text = (
            f"There are {male_count} males and {female_count} females in the frame. "
            f"{'Someone has raised their hand.' if hand_raise_detected else 'No hand raise detected.'} "
            f"Summarize this for a security report."
        )

        try:
            chat_completion = groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant summarizing surveillance data."},
                    {"role": "user", "content": prompt_text}
                ],
                model="llama3-8b-8192",
            )
            summary = chat_completion.choices[0].message.content
        except Exception as e:
            summary = f"Error from Groq: {e}"

        frame = cv2.resize(frame, (720, 480))
        if frame_placeholder and log_placeholder:
            frame_placeholder.image(frame, channels="BGR")
            log_placeholder.markdown(f"*👥 Gender Summary:* {male_count} male(s), {female_count} female(s)  \n"
                                     f"🙋 Hand Raised: {'Yes' if hand_raise_detected else 'No'}  \n"
                                     f"📄 *Groq Summary:* {summary}")

        time.sleep(0.2)

    cap.release()
    pose.close()