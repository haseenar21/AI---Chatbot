import streamlit as st
from practicebot import get_response

st.title("🤖 AI Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.write(msg)

prompt = st.chat_input("Type your message")

if prompt:
    st.session_state.history.append(("user", prompt))

    with st.chat_message("user"):
        st.write(prompt)

    reply = get_response(prompt)

    st.session_state.history.append(("assistant", reply))

    with st.chat_message("assistant"):
        st.write(reply)