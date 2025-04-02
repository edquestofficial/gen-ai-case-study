from dotenv import load_dotenv
import os
from llama_index.core import Settings, VectorStoreIndex, StorageContext
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

def generate_answers(question):
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
        
    if not api_key:
        raise ValueError("API key for Gemini model is not set.")
        
    # Initialize the Gemini embedding model
    embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
        
    # Initialize the Gemini language model
    llm = Gemini(api_key=api_key, model_name="models/gemini-pro")
        
    # Set Global settings
    Settings.llm = llm
    Settings.embed_model = embedding_model

    # Load the ChromaDB client
    client = chromadb.PersistentClient(path='./chroma_db')
        
    # Fetch the collection from ChromaDB
    chroma_collection = client.get_collection("quickstart")
        
    # Fetch the vector store from the collection
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        
    # Create a storage context
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
    # Get the index from the vector store
    index = VectorStoreIndex.from_vector_store(vector_store)

    query_engine = index.as_query_engine()
    return query_engine.query(question)