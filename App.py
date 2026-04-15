import streamlit as st
from transformers import pipeline
def load_summarizer():
    returns pipeline("Summarization", model="Falconsai/text_summarization")
  summarizer = load_summarizer()

st.title(" AI text Summarizer")
st.write("Enter a long text below, and get a concise summary!")
