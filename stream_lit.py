from google import genai
import streamlit as st

client = genai.Client(api_key='AQ.Ab8RN6JN7tANZnPuyz5mKpRIUV6FPzQ97ppr2E77-1J5GC5qsQ')

st.title("Talk to Chatbot")
st.write("This app demonstrates a conversational agent.")

user_input = st.text_input("Ask a question:")
if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        response = client.models.generate_content(
            model='gemini-3.1-flash-lite', contents=user_input,
            
        )
    st.write(response.text)
