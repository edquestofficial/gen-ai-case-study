from dotenv import load_dotenv
import os
import chromadb
from llama_index.core import (
    Settings, StorageContext, VectorStoreIndex
)
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore


def generate_embeddings(data):
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
        
    # Set embedding and language models
    embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    llm = Gemini(api_key=api_key, model_name="models/gemini-pro")

    # Load documents
    documents = data
        
    # Create a client and a new collection
    client = chromadb.PersistentClient(path='./chroma_db')
    chroma_collection = client.get_or_create_collection("quickstart")

    # Create a vector store
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    # Create a storage context
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Set Global settings
    Settings.llm = llm
    Settings.embed_model = embedding_model

    # Create an index from the documents and save it to the disk
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context
    )