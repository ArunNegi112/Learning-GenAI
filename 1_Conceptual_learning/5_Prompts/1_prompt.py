import streamlit as st 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.5)



#We are trying to create a simple research assistant bot, but it is not possible if we only let the user give prompt called - Static prompt (as we have done before) 

#we will have to first tell the model about who he is and what are the expectations from him called - Dynamic prompt



st.header("Summarizer assistant")
st.markdown("_Static prompt_")
#Using static prompt
userinput = st.text_input("Enter the text")
if st.button("Summarize"):
    response = model.invoke(userinput)
    st.write(response.content)



from langchain_core.prompts import PromptTemplate, load_prompt

st.header("Summarizer Assistant 2")
st.markdown("_Dynamic prompt_")
#Using dynamic prompt

text = st.text_input("Enter the text:")
length = st.text_input("What should be the length of summary")
focus = st.text_input("What should the summary focus on?")
format = st.selectbox(label="Output Format",options=['Paragraph','Bullet Points'])

template = load_prompt(r"1_Conceptual_learning\5_Prompts\template.json")

prompt = template.invoke(input={
    'input_text':text,
    'desired_length':length,
    'optional_focus':focus,
    'output_format':format
})

if st.button("Summarize",key=2):
    response = model.invoke(prompt)
    st.write(response.content)