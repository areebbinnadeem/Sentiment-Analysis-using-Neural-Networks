import streamlit as st
import json
import os
from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import numpy as np

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the tokenizer
tokenizer_path = os.path.join(current_dir, 'tokenizer.json')
with open(tokenizer_path) as f:
    tokenizer_config = json.load(f)
    tokenizer_json = json.dumps(tokenizer_config)  # Convert dictionary to JSON string
    tokenizer = tokenizer_from_json(tokenizer_json)

# Load the model
model_path = os.path.join(current_dir, 'cnn_model.h5')
model = load_model(model_path)

# Tokenizer configuration
MAX_SEQUENCE_LENGTH = 500

def predict_sentiment(review):
    sequences = tokenizer.texts_to_sequences([review])
    data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
    prediction = model.predict(data)
    sentiment = 'Positive' if prediction[0] > 0.5 else 'Negative'
    return sentiment

# Streamlit UI
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 10px;
    }
    .title {
        text-align: center;
        color: #4CAF50;
        font-family: 'Arial', sans-serif;
        font-size: 2.5em;
    }
    .textarea {
        width: 100%;
        height: 200px;  /* Set height directly */
        padding: 12px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        margin-top: 6px;
        margin-bottom: 16px;
        resize: vertical;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #45a049;
    }
    .result {
        font-size: 1.5em;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<h1 class="title">Sentiment Analysis Web App</h1>', unsafe_allow_html=True)

st.write("Enter a movie review to predict its sentiment.")
review = st.text_area("Review", height=200)  # Remove the style argument

if st.button("Predict"):  # Remove the class_ argument
    sentiment = predict_sentiment(review)
    st.markdown(f'<p class="result">Sentiment: {sentiment}</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
