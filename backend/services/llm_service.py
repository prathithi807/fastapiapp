from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",   # or another Groq-supported model
    temperature=0.5,
)

def llm_response(question: str):
    response = model.invoke(question)
    return response.content