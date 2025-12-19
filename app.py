import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write

from speech.stt import speech_to_text
from speech.tts import text_to_speech
from agent.planner import planner
from agent.executor import executor
from agent.evaluator import evaluator
from memory.memory_manager import Memory

memory = Memory()

st.title("🗣️ मराठी सरकारी योजना सहाय्यक")

if st.button("🎙️ बोला"):
    fs = 16000
    duration = 6
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write("input.wav", fs, recording)

    user_text = speech_to_text("input.wav")
    st.write("आपण म्हणालात:", user_text)

    plan = planner(user_text, memory)
    result = executor(plan, memory)
    response = evaluator(result)

    text_to_speech(response)
