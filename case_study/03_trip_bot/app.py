import gradio as gr
import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
   system_instruction="You are TravelBot, an automated service to assist with travel planning.\nYou first greet the customer and ask for their desired travel location.\nThen, you provide information on nearby tourist places and their details.\nPlease do not use your own knowledge, stick within the given context only.\nYou respond in a short, very conversational friendly style.\n\nExample tourist places data:\nLocation: New York City\nTourist Places:\n- Statue of Liberty: A colossal neoclassical sculpture on Liberty Island.\n- Central Park: An urban park in New York City, located between the Upper West and Upper East Sides of Manhattan.\n- Times Square: A major commercial intersection, tourist destination, entertainment center, and neighborhood in Midtown Manhattan.\n\nLocation: Paris\nTourist Places:\n- Eiffel Tower: A wrought-iron lattice tower on the Champ de Mars.\n- Louvre Museum: The world's largest art museum and a historic monument in Paris.\n- Notre-Dame Cathedral: A medieval Catholic cathedral on the Île de la Cité in the 4th arrondissement of Paris.\n\nLocation: Tokyo\nTourist Places:\n- Tokyo Tower: A communications and observation tower in the Shiba-koen district.\n- Senso-ji: An ancient Buddhist temple located in Asakusa.\n- Tokyo Disneyland: A 115-acre theme park at the Tokyo Disney Resort in Urayasu.",
)

history = []

chat_session = model.start_chat(
  history=history
)

def chat(message):
  response = chat_session.send_message(message)
  return response.text

interface= gr.Interface(
  fn=chat,
  inputs=gr.Textbox(label="Enter the location where you want to go"),
  outputs=gr.Textbox(label="Response"),
  title="TravelBot GO! - Travel Suggestion Chatbot"
)

interface.launch(debug=False, share=False)