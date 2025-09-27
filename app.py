import streamlit as st
from huggingface_hub import InferenceApi

st.title("Mini Character AI")

API_KEY = "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"

# Modello pubblico gratuito
api = InferenceApi(repo_id="EleutherAI/gpt-neo-125M", token=API_KEY)

personaggi = {
    "Assistente gentile": "Sei un assistente molto gentile e disponibile.",
    "Critico sarcastico": "Rispondi con sarcasmo e ironia.",
    "Esperto fantasy": "Parli come un esperto di mondi fantasy."
}

personaggio = st.selectbox("Scegli un personaggio:", list(personaggi.keys()))
prompt_personaggio = personaggi[personaggio]

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Scrivi qualcosa:")

if user_input:
    full_prompt = f"{prompt_personaggio}\nUtente: {user_input}\nAI:"
    response = api(inputs=full_prompt)
    st.session_state.messages.append({"user": user_input, "ai": response})

for chat in st.session_state.messages:
    st.write("**Tu:**", chat["user"])
    st.write(f"**{personaggio}:**", chat["ai"])
