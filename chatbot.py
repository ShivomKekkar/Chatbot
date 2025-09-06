import streamlit as st
from openai import OpenAI

# Load API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["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"])

st.set_page_config(page_title="ChatGPT Web Chatbot", page_icon="🤖")
st.title("🤖 ChatGPT Web Chatbot")

# Keep chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful chatbot."}
    ]

# Show chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**🤖 Bot:** {msg['content']}")

# User input
user_input = st.text_input("Type your message:")

if st.button("Send") and user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Query OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state["messages"]
    )
    reply = response.choices[0].message.content

    # Add bot reply
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.experimental_rerun()
