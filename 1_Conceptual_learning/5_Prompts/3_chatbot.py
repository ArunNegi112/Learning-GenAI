"""
Creating a simple chatbot with chat history 
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.8)
chat_history = [
    SystemMessage(content="You are a helpful gym trainer that will guide the user to get their dream physic. But respond in only 30 words or less")
]

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    chat_history.append(HumanMessage(content=user_input))

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI: ", response.content)

print(chat_history)