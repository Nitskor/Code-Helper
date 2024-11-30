import streamlit as st
import os
from langchain_groq import ChatGroq


sec_key = os.environ.get("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.1-70b-versatile",temperature=0,groq_api_key = sec_key)
#result = llm.invoke("Hi")
#print(result.content)

if 'previous_questions' not in st.session_state:
    st.session_state.previous_questions = []
if 'previous_answers' not in st.session_state:
    st.session_state.previous_answers = []

if st.session_state.previous_questions:
    with st.expander("Previous Questions and Answers"):
        for i in range(len(st.session_state.previous_questions)):
            st.write(f"**Question {i+1}**: {st.session_state.previous_questions[i]}")
            st.code(st.session_state.previous_answers[i], language='markdown')
            st.write("\n")

with st.form("Code Helper"):
    # Your form fields here
    question = st.text_input("How can I help you?")      
    submit_button = st.form_submit_button("Submit")
    
clear_button = st.checkbox("Clear Previous Questions and Answers")

#st.title("Code Helper")
#question = st.text_input("How can I help you?")
#submit_button = st.button(key="Submit")

if submit_button:  
  result = llm.invoke(question)
  answer = result.content  
  st.session_state.previous_questions.append(question)
  st.session_state.previous_answers.append(answer)   
  st.code(answer,language='markdown')

if clear_button:
    st.session_state.previous_questions = []
    st.session_state.previous_answers = []
