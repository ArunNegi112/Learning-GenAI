"""
MessagePlaceholder helps to inject previous chats into the conversation dynamically.
message placeholder represents place where a list of messages will be inserted
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#Create chat template
template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
    ])


#Get the chat history
chat_history = []
with open(r"1_Conceptual_learning\5_Prompts\chat_history.txt",'r') as f:
    chat_history.extend(f.readlines())


print(chat_history)
#invoke the template
query = 'How long do i have to wait for refund?'
prompt = template.invoke({'chat_history':chat_history,'query':query})

print(prompt)


