# Marathi Voice Agent 🎙️🇮🇳

A **voice-first AI assistant** that understands **Marathi speech**, processes the request using **Google Gemini models**, and responds back **in Marathi voice**.

This project is built to demonstrate:
- Voice-based interaction (no text-only chatbot)
- Native Indian language support (Marathi)
- End-to-end speech → AI → speech pipeline

---

## 🚀 Features

- 🎤 **Voice Input**  
  User speaks in Marathi using microphone

- 🧠 **AI Reasoning (Gemini)**  
  Audio/text is processed using Google Gemini models

- 🔊 **Voice Output (Marathi)**  
  AI response is converted back to Marathi speech

- 🗣️ **Fully Voice-First System**  
  No hard-coded responses  
  No text-only flow

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Google Gemini API**
- **Speech Recognition**
- **Text-to-Speech (TTS)**
- **Whisper / Audio Processing**
- **Streamlit (optional UI)**

---

## 📂 Project Structure

marathi_voice_agent/
│
├── app.py # Main application entry
├── agent/ # Gemini AI logic
│ └── agent.py
│
├── memory/ # Conversation memory handling
│ └── memory.py
│
├── speech/ # Speech-to-text and text-to-speech
│ ├── stt.py
│ └── tts.py
│
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files (venv, cache, etc.)
└── README.md # Project documentation


---

## 🔄 How It Works (Step-by-Step)

1. **User speaks in Marathi**
2. Audio is captured from the microphone
3. Speech is converted to text
4. Text is sent to **Gemini AI**
5. Gemini generates a response in Marathi
6. Response is converted to speech
7. User hears the answer in Marathi

---

## 🧠 Gemini Models Used

- `gemini-2.5-flash`
- `gemini-flash-latest`
- (Model can be changed easily)

---

## 🔑 API Key Setup

Create a Gemini API key from Google AI Studio.

Then add it in your code:

```python
API_KEY = "YOUR_GEMINI_API_KEY"

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/Shinu87/marathi-voice-agent.git
cd marathi-voice-agent

2️⃣ Create Virtual Environment
python -m venv marathi_ai


Activate:

Windows

marathi_ai\Scripts\activate


Linux / Mac

source marathi_ai/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py


🎧 Speak in Marathi and listen to the response!
