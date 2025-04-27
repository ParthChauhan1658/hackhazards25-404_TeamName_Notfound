![github-submission-banner](https://github.com/user-attachments/assets/a1493b84-e4e2-456e-a791-ce35ee2bcf2f)

# 🚀 Project Title

> Smart Surveillance: Gender Classification and Aggression Detection Using AI.

---

## 📌 Problem Statement
 
**Problem Statement 1 – Weave AI magic with Groq**

---

## 🎯 Objective

🎯 Problem Statement & Use Case
This project addresses the growing need for automated surveillance systems capable of detecting gender-based threats and violent behavior in real-time. In public places like parks, campuses, transportation hubs, and office buildings, it is often difficult for security personnel to monitor all areas at once, especially in high-traffic zones.

👥 Who It Serves
This system is designed for:
- Security agencies
- Smart city planners
- Campus safety departments
- Organizations focused on women’s safety
- Developers or researchers in AI for social impact

🌍 Real-World Use Case
By combining gender detection, proximity analysis, and violence recognition, this tool helps identify:
- Situations where a woman is surrounded by multiple men (potential harassment risk)
- Instances of physical violence or aggression
- Events that should trigger real-time alerts and be summarized for security reports

✅ Value It Provides
Enhances public safety through AI-powered monitoring
- Sends timely alerts via SMS for fast response
- Provides natural-language incident summaries using Groq's LLM
- Supports both offline video analysis and real-time insights
- Reduces manual workload for security teams and improves situational awareness

---

## 🧠 Team & Approach

### Team Name:  
`404_TeamName_Notfound`

### Team Members:  
- Parth Chauhan ([GitHub](https://github.com/ParthChauhan1658) / [LinkedIn](www.linkedin.com/in/parth-chauhan-6bbb69295) / ML developer)  
- Krishnendu Nair ([GitHub](https://www.linkedin.com/in/krishnendu-nair235/) / [LinkedIn](https://github.com/KrishnenduNair) / ML developer)

### Your Approach:  
- Why We Chose This Problem- 
  With the rise in safety concerns across public and semi-public spaces, especially involving gender-based harassment and violent behavior, we saw an urgent need for a proactive, AI-      powered surveillance solution. Traditional systems rely heavily on manual monitoring, which is both labor-intensive and prone to human error. Our goal was to augment security systems    with real-time detection and alerting to help protect vulnerable individuals—especially women—in crowded or isolated environments. 
- Key challenges-
  - Real-time gender detection: Classifying individuals as male or female using visual data under variable lighting, angles, and movement.
  - Surrounding detection logic: Designing a spatial logic to detect when a woman is being encircled or outnumbered by men.
  - Violence recognition: Incorporating a pre-trained model to recognize patterns of aggressive or violent behavior in video frames.
  - Timely alerting: Ensuring alerts are triggered at the right time without false positives and sending SMS notifications via Twilio.
  - Natural-language summaries: Generating clear, human-readable incident reports using LLMs (Groq in this case).
  
- Pivots, brainstorms, or breakthroughs during hacking
  - Originally, the idea was just gender classification, but during brainstorming we realized that identifying potential threats based on social dynamics (like a lone woman being       surrounded) could add much more value.
  - A major breakthrough came with the integration of a violence detection model, which allowed us to move beyond passive monitoring to actual risk detection.
  - We debated using OpenAI/GPT, but discovered Groq’s LLM was faster for summarizing frame-level insights, which made it perfect for real-time or near-real-time use cases.
  - Lastly, combining everything into a streamlit UI helped make the tool accessible for non-technical users—something we felt was essential for deployment in actual safety centers.

---

## 🛠️ Tech Stack

### Core Technologies Used:
- Frontend: Streamlit, OpenCV
- Backend: Python, OpenCV, TensorFlow/Keras, Roboflow SDK, Groq API, Twilio API
- Database: None
- APIs: Roboflow API, Groq API, Twilio API
- Hosting: Localhost, Streamlit Cloud, GitHub

### Sponsor Technologies Used :
- [✅] **Groq:** _In this project, Groq's Large Language Model (LLM) is used to generate natural language summaries of surveillance events. After each frame is processed and individuals are detected using the Roboflow model, a prompt is dynamically created describing the number of males and females detected, and whether a woman appears to be surrounded. This prompt is then sent to Groq's API, which responds with a simple, human-readable summary suitable for a security report. These summaries help security teams quickly understand potential threats without needing to manually review every frame or raw detection data._  
---

## ✨ Key Features

Highlight the most important features of your project:

- ✅ Gender Classification: Detects and classifies individuals as male or female in each video frame using a Roboflow-trained model. 
- ✅ Woman Surrounded Detection: Identifies if a woman is surrounded by multiple men within a proximity threshold and triggers real-time alerts via SMS.
- ✅ Violence Detection: Uses a deep learning model (Keras/TensorFlow) to detect violent activities in video footage and logs critical alerts automatically. 
- ✅ Real-time Alerts: Sends immediate SMS alerts for critical events using Twilio, ensuring quick response times.
- ✅ Natural Language Summarization: Groq API is used to summarize surveillance events into clear, professional security reports.
- ✅ User-Friendly Interface: Simple web-based dashboard built using Streamlit for video upload, processing, and viewing event summaries.
- ✅ Automated Logging: Critical events (like violence detection) are logged automatically for record-keeping.

[Demo Images](https://github.com/user-attachments/assets/1cf831dc-ae42-4fa8-9a8d-717c816de309)

---

## 📽️ Demo & Deliverables

- **Demo Video Link:** [Paste YouTube or Loom link here]  
- **Pitch Deck / PPT Link:** [PDF](https://github.com/ParthChauhan1658/hackhazards25-404_TeamName_Notfound/raw/main/Hackhazards_25.pdf) 

---

## ✅ Tasks & Bonus Checklist

- [✅] **All members of the team completed the mandatory task - Followed at least 2 of our social channels and filled the form** 
- [✅] **All members of the team completed Bonus Task 1 - Sharing of Badges and filled the form (2 points)**  
- [✅] **All members of the team completed Bonus Task 2 - Signing up for Sprint.dev and filled the form (3 points)**  
*(Mark with ✅ if completed)*

---

## 🧪 How to Run the Project

### Requirements:
- **Python 3.9+**
- **Streamlit** for UI
- **OpenCV** for video processing
- **NumPy** for array and matrix operations
- **Pytz** for timezone handling
- **Python-dotenv** for environment variable management
- **Twilio** for sending SMS alerts
- **Roboflow** for AI gender detection model integration
- **Groq** for summarizing detected events via LLM

### Local Setup:
```bash
# Clone the repo
git clone https://github.com/ParthChauhan1658/hackhazards25-404_TeamName_Notfound.git

# Navigate into the project directory
cd hackhazards25-404_TeamName_Notfound

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# For Windows:
venv\Scripts\activate
# For Mac/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Start the Streamlit development server
streamlit run app.py
```


---

## 🏁 Final Words

Participating in Hackhazards 2.5 was an incredibly rewarding experience. Our team tackled the challenge of building an AI-powered surveillance system aimed at enhancing women's safety, integrating technologies like Roboflow for gender detection, Groq for intelligent summarization, and Twilio for real-time SMS alerts. Setting up real-time video processing, fine-tuning the detection models, and managing asynchronous operations were significant technical hurdles that pushed us to deepen our understanding of Python’s capabilities. Despite late-night debugging sessions and a few unexpected alerts during testing, the journey was filled with learning, collaboration, and memorable moments. Special thanks to the organizers for providing such a dynamic platform, and a huge shout-out to my team members for their relentless effort and innovation throughout the event.

---
