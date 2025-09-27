import streamlit as st
from huggingface_hub import InferenceApi

st.title("Mini Character AI")

# API Key Hugging Face
API_KEY = "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"

# Crea l'oggetto InferenceApi per il modello Falcon 7B Instruct
api = InferenceApi(repo_id="google/flan-t5-large", token=API_KEY)

# Mantieni la conversazione nello stato della sessione
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input dell’utente
user_input = st.text_input("Scrivi qualcosa:")

if user_input:
    # Chiamata all’AI tramite Hugging Face
    response = api(inputs=user_input)
    st.session_state.messages.append({"user": user_input, "ai": response})

# Mostra la conversazione
for chat in st.session_state.messages:
    st.write("**Tu:**", chat["user"])
    st.write("**AI:**", chat["ai"])
