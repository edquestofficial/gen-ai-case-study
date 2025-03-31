import gradio as gr
import google.generativeai as genai
from src import utils as ut

# Configure the Gemini API
genai.configure(api_key="AIzaSyAOLyWRegqB-NxufjTlkyRBhn1ESJE-G38")
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Set up the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
     ut.system_instruction  
    ),
)

chat = model.start_chat(
  history=[
  ]
)

def get_response(prompt):
  response = chat.send_message(prompt)
  return response.text

def chatbot(message, history):
  response = get_response(message)
  return response

gr.ChatInterface(fn=chatbot, title="PathFinder - Career Guidance Chatbot").launch(debug=True, share=True)