import os
import shutil
import logging
import json
import gradio as gr
from dotenv import load_dotenv
from llama_index.core import Settings, SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Get the Gemini API key from the environment variable
gemini_api_key = os.getenv('GEMINI_API_KEY')

# Initialize models and settings
gemini_embedding_model = GeminiEmbedding(api_key=gemini_api_key, model_name="models/embedding-001")
llm = Gemini(api_key=gemini_api_key, model_name="models/gemini-pro")
Settings.llm = llm
Settings.embed_model = gemini_embedding_model

# Define the upload directory
UPLOAD_DIR = "./data"

def process_document():
    """Load documents, create vector store and index, and return query engine."""
    documents = SimpleDirectoryReader(UPLOAD_DIR).load_data()
    client = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = client.get_or_create_collection("quickstart")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    return index.as_query_engine()

def upload_file(file):
    """Handle file upload and processing."""
    logger.debug("Upload function called")
    
    logger.info(f"File object received: {file}")
    logger.debug(f"File name: {file.name}")

    filename = os.path.basename(file.name)
    logger.info(f"Original filename: {filename}")

        # Create the full path for the uploaded file
    file_path = os.path.join(UPLOAD_DIR, filename)
    logger.info(f"Destination file path: {file_path}")

        # Copy the uploaded file to the destination
    logger.debug("Attempting to copy file")
    shutil.copy(file.name, file_path)

        # Verify if the file was actually copied
    if os.path.exists(file_path):
        logger.info(f"File successfully copied to {file_path}")
        file_size = os.path.getsize(file_path)
        logger.info(f"Uploaded file size: {file_size} bytes")
        # Process the uploaded file
        global query_engine
        query_engine = process_document()
        return json.dumps({"message": f"File '{filename}' uploaded successfully to {file_path}. Size: {file_size} bytes. You can now ask your query."})
       
def ask_query(query):
    question = (
        f"You are a JSON parser which gives response in extracting and providing information from "
        f"invoice PDF documents in response to user queries. The system accepts user questions "
        f"regarding specific invoice details and returns the relevant data in a standardized JSON format. "
        f"Make sure if the user asks multiple queries, then the output will be in new lines. Do not give "
        f"output in a single line output.\n The user query is: {query}"
    )

    response = query_engine.query(question)
    # Format the response in the desired format
    response_text = str(response)

    # Convert the JSON-like response string into a proper format with new lines
    response_json = response_text.replace("\\n", "\n")

    return response_json

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# PDF Upload and Query System")

    with gr.Tab("Upload File"):
        file_input = gr.File(label="Choose a PDF file to upload")
        upload_output = gr.Textbox(label="Upload Result")
        upload_button = gr.Button("Upload")

    with gr.Tab("Ask a Query"):
        query_input = gr.Textbox(label="Enter your query")
        query_output = gr.TextArea(label="Query Result", lines=10)
        query_button = gr.Button("Submit Query")

    upload_button.click(upload_file, inputs=file_input, outputs=upload_output)
    query_button.click(ask_query, inputs=query_input, outputs=query_output)

# Launch the interface
demo.launch(debug=True)

logger.info("Gradio interface launched")
