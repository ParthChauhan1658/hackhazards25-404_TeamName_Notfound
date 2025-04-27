import streamlit as st
import tempfile
from genderclassification import gender_classification_main
from violencedetection import violence_detection_main  # Assuming you've saved your violence detection code in this file

st.title("👁️ Gender & Threat Detection")

# Upload video
video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if video_file is not None:
    st.video(video_file)

    # Option to choose between gender estimation or violence detection
    analysis_option = st.radio(
        "Select the analysis to perform",
        ("Estimate Gender", "Detect Violence")
    )

    if st.button("Start Analysis"):
        with open("uploaded_video.mp4", "wb") as f:
            f.write(video_file.read())

        frame_placeholder = st.empty()
        log_placeholder = st.empty()

        st.info("⏳ Processing video. This may take a few minutes...")

        # Perform the selected analysis
        if analysis_option == "Estimate Gender":
            gender_classification_main("uploaded_video.mp4", frame_placeholder, log_placeholder)
        elif analysis_option == "Detect Violence":
            violence_detection_main("uploaded_video.mp4", frame_placeholder, log_placeholder)

        st.success("✅ Done analyzing the video.")



