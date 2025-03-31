from pinecone import Pinecone
from google import genai
from langchain.text_splitter import CharacterTextSplitter
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 


def conn_pinecorn():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    return pc
def conn_gemini():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return client
