from dotenv import load_dotenv
import streamlit as st
import os
from openai import OpenAI

load_dotenv()
MODEL = 'gpt-4o'
open_api_key = ""

st.title('AI AUDIO ANALYZER')
audio_format = ['mp3','wav','m4a']
audio_file = st.file_uploader('upload an audio file',type= audio_format)

if audio_file:
    st.audio(audio_file)

    transcription = open_api_key.audio.transcription.create(
        model = 'whisper-1',
        file = audio_file
    )

    response = open_api_key.chat.completions.create(
    model=MODEL,  # Replace MODEL with your actual model identifier
    messages=[
        {"role": "system", "content": "You are an audio analyzer AI. Analyze the audio and create a summary of the provided transcription. Respond in Markdown."},
        {"role": "user", "content": f"The audio transcription is: {transcription.text}"}
    ],
    temperature=0  # Temperature parameter for response generation
    )
    st.markdown(response['choices'][0]['message']['content'])

# Assuming response.choices[0].messages.content is a string in Markdown format
# Print the Markdown content using st.markdown if you are using Streamlit

