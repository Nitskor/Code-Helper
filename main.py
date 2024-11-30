import streamlit as st
import os
from langchain_groq import ChatGroq


sec_key = os.environ.get("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.1-70b-versatile",temperature=0,groq_api_key = sec_key)
#result = llm.invoke("Hi")
#print(result.content)

st.title("Code Helper")
question = st.text_input("How can I help you?")
submit_button = st.button("Submit")

if submit_button:
  result = llm.invoke(question)
  st.code(result.content,language='markdown')
