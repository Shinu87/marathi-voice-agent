from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang="mr")
    filename = "response.mp3"
    tts.save(filename)
    os.startfile(filename)  # Windows-safe audio playback
