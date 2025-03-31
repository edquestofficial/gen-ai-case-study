from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from IPython.display import Markdown, display
import chromadb
from llama_index.llms.gemini import Gemini
import gradio as gr
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
llm = Gemini(api_key=api_key, model_name="models/gemini-1.5-flash")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Load from disk
db2 = chromadb.PersistentClient(path="./chroma_db1")
chroma_collection = db2.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embed_model,
)
Settings.llm = llm

# Query Data from the persisted index
query_engine = index.as_query_engine()
response = query_engine.query("tell me about the superlinear returns")
print(response)
# display(Markdown(f"<b>{response}</b>"))

def chat(message):
    response = query_engine.query(message)
    return response

interface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(label="Enter your message"),
    outputs=gr.Textbox(label="Response"),
    #title="Chatbot Interface"
)

interface.launch(debug=False, share=False)