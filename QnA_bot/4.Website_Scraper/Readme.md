Gen AI QnA Bot for Website Scraper
This project demonstrates how to create a QnA bot using Gen AI for scraping website content and providing answers based on the extracted data. The bot utilizes the Gemini model for natural language processing and Gradio for the user interface.

Prerequisites
Python 3.7+
Required libraries:
requests
beautifulsoup4
llama-index
html2text
langchain
llama-index-llms-gemini
llama-index-embeddings-huggingface
google-generativeai
llama-index-llms-ollama
llama-index-vector-stores-chroma
gradio
dotenv


Setup Instructions
Install Required Libraries


pip install requests beautifulsoup4 llama-index html2text
pip install langchain
pip install llama-index-llms-gemini
pip install llama-index-embeddings-huggingface
pip install google-generativeai
pip install llama-index-llms-ollama
pip install llama-index-vector-stores-chroma
pip install gradio
pip install python-dotenv
Set Up the Environment

Ensure you have your Gemini API key set up in a .env file in your project directory:

GEMINI_API_KEY=your_gemini_api_key


Step 1: Scrape Website Data
   This step involves extracting textual content from a specified URL and saving it locally in .txt files.
   
Step 2: Load Data and Create Index
   This step involves loading the data from the local directory, creating the vector store index, and setting up the query engine.

Step 3: Create Vector Store Index and Query Engine
   This step involves setting up the vector store index using the extracted data and initializing the query engine.

   
