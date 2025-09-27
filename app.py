import streamlit as st
from transformers import pipeline

st.title("Mini Character AI")

# Se vuoi usare la tua Hugging Face API Key
# import os
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "LA_TUA_API_KEY"

# Modello AI online
chatbot = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Scrivi qualcosa:")

if user_input:
    response = chatbot(user_input, max_length=200, do_sample=True, temperature=0.7)
    st.session_state.messages.append({"user": user_input, "ai": response[0]["generated_text"]})

# Mostra conversazione
for chat in st.session_state.messages:
    st.write("**Tu:**", chat["user"])
    st.write("**AI:**", chat["ai"])
