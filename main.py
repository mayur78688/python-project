import streamlit as st
import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from gtts import gTTS
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()  # Add your OpenAI API key here

def record_audio(filename):
    fs = 44100
    duration = 5  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2, dtype='float64')
    st.write("Recording Audio...")
    sd.wait()
    st.write("Audio recording complete. Playing Audio...")
    sd.play(myrecording, fs)
    sd.wait()
    write(filename, fs, myrecording)  # Save as WAV file
    st.write("Audio playback complete.")

def speech_to_text(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    st.write(result["text"])
    return result["text"]

def get_llm_response(text):
    completion = client.chat_completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a chat bot"},
            {"role": "user", "content": text}
        ]
    )
    response_text = completion.choices[0].message['content']
    st.write(response_text)
    return response_text

def text_to_speech(text):
    # Language in which you want to convert
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named welcome 
    myobj.save("welcome.mp3")
    # Playing the converted file
    os.system("mpg321 welcome.mp3")

def main():
    st.title("Chat Bot Application")
    st.write("Click the button below to start recording.")

    if st.button("Start Recording"):
        filename = 'output.wav'
        record_audio(filename)
        text = speech_to_text(filename)
        response_text = get_llm_response(text)
        text_to_speech(response_text)

if __name__ == "__main__":
    main()
