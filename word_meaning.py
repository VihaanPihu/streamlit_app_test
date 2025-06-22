import pandas as pd
import random
import requests
from gtts import gTTS
import io
import streamlit as st
from deep_translator import GoogleTranslator

# Load 500-word CSV
words = pd.read_csv("/home/vihaan/coding/pihu_project/500_words_flashcards.csv", header=None)

# Safely select a random word
row_max, col_max = words.shape
random_row = random.randint(0, row_max - 1)
random_col = random.randint(0, col_max - 1)
random_word = str(words.iloc[random_row, random_col]).strip().upper()

# Dictionary meaning (optional use)
try:
    word_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{random_word}")
    word_data = word_response.json()[0]
except:
    word_data = {}

# Translate using deep_translator
try:
    translated_text = GoogleTranslator(source='en', target='hi').translate(random_word)
except:
    translated_text = "अनुवाद नहीं मिला"

# Get image from Pexels API
API_KEY = "RvjzTpc3GthjpLJx6UQV5GJ2qsjAbISomd7CvgXlyE8wx63nXSrfCI3G"
image_url = ""

try:
    headers = {"Authorization": API_KEY}
    image_response = requests.get(f"https://api.pexels.com/v1/search?query={random_word}&per_page=1", headers=headers)
    image_data = image_response.json()
    image_url = image_data['photos'][0]['src']['small']
except:
    image_url = ""

# --- Streamlit UI ---
st.title("📚 Word Game")
col1, col2 = st.columns(2)

# English column
with col1:
    st.error(f"English: {random_word}")
    try:
        tts = gTTS(text=random_word, lang='en')
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        st.audio(audio_buffer, format='audio/mp3')
    except:
        st.warning("🔇 English audio not available")

# Hindi column
with col2:
    st.success(f"Hindi: {translated_text}")
    try:
        tts_hi = gTTS(text=translated_text, lang='hi')
        audio_buffer_hi = io.BytesIO()
        tts_hi.write_to_fp(audio_buffer_hi)
        audio_buffer_hi.seek(0)
        st.audio(audio_buffer_hi, format='audio/mp3')
    except:
        st.warning("🔇 Hindi audio not available")

# Image
st.markdown("---")
if image_url:
    st.image(image_url, caption=random_word)
else:
    st.info("🖼️ No image found")

# Next button
if st.button("Next"):
    pass
