from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model = ChatGroq(model = "llama-3.3-70b-versatile")

messages = [
    SystemMessage(content = "you are a very practical and fact saying bot. you say what the real matter is")
]

def get_response(prompt):
    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    return response.content

