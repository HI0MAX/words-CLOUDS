import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("Word Generator")

uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode('utf-8')
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    st.image(wordcloud.to_array(), use_column_width=True, caption="Generated Word Cloud")
    st.subheader("Raw Text:")
    st.text(text)
else:
    st.info("Upload a text file to generate a word cloud.")
