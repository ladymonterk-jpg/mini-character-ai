import streamlit as st
from huggingface_hub import InferenceApi

st.title("Mini Character AI")

# API Key Hugging Face
API_KEY = "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"

# Crea l'oggetto InferenceApi con un modello pubblico funzionante
api = InferenceApi(repo_id="google/flan-t5-large", token=API_KEY)

# Definisci i personaggi
personaggi = {
    "Assistente gentile": "Sei un assistente molto gentile e disponibile.",
    "Critico sarcastico": "Rispondi con sarcasmo e ironia.",
    "Esperto fantasy": "Parli come un esperto di mondi fantasy."
}

#
