def violence_detection_main(video_path, frame_placeholder=None, log_placeholder=None):
    import cv2, time
    import numpy as np
    import mediapipe as mp
    from roboflow import Roboflow
    from groq import Groq

    # Initialize models
    rf = Roboflow(api_key="waM5IrbdSRqBjOLWJFmx")  # Replace with your API key
    project = rf.workspace().project("gender-bkoji")  # Replace with your project name
    model = project.version(1).model

    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_drawing = mp.solutions.drawing_utils

    groq_client = Groq(api_key="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")  # Replace with your Groq API key

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        try:
            result = model.predict(frame, confidence=40, overlap=70).json()
            predictions = result.get("predictions", [])
            violence_detected = False

            for pred in predictions:
                # Check for violence detection in predictions
                label = pred['class']
                if label == 'violence':  # Adjust based on your model's class
                    violence_detected = True
                    x, y, w, h = int(pred['x']), int(pred['y']), int(pred['width']), int(pred['height'])
                    cv2.rectangle(frame, (x - w//2, y - h//2), (x + w//2, y + h//2), (0, 0, 255), 2)  # Red for violence
                    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
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
            f"Violence detected: {'Yes' if violence_detected else 'No'}. "
            f"{'Someone has raised their hand.' if hand_raise_detected else 'No hand raise detected.'} "
            f"Summarize this for a security report."
        )

        try:
            chat_completion = groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant summarizing surveillance data."},
                    {"role": "user", "content": prompt_text}
                ],
                model="llama3-8b-8192",  # Adjust to use an appropriate model for your case
            )
            summary = chat_completion.choices[0].message.content
        except Exception as e:
            summary = f"Error from Groq: {e}"

        frame = cv2.resize(frame, (720, 480))
        if frame_placeholder and log_placeholder:
            frame_placeholder.image(frame, channels="BGR")
            log_placeholder.markdown(f"*⚠️ Violence Detected:* {'Yes' if violence_detected else 'No'}  \n"
                                     f"🙋 Hand Raised: {'Yes' if hand_raise_detected else 'No'}  \n"
                                     f"📄 *Groq Summary:* {summary}")

        time.sleep(0.2)

    cap.release()
    pose.close()
