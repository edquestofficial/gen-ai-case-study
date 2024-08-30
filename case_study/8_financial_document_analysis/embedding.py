from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.gemini import Gemini
import os
from dotenv import load_dotenv

load_dotenv()
# Configure api_key
GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")

# Load the HuggingFace embedding model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

Settings.llm = Gemini(api_key=GEMINI_API_KEY, model_name="models/gemini-pro")

# Load documents
documents = SimpleDirectoryReader("./data").load_data()
print(f"Number of documents loaded: {len(documents)}")

# Generate embeddings for each document
document_embeddings = [embed_model.get_text_embedding(doc.get_text()) for doc in documents]

# Print embeddings for all documents
for i, embedding in enumerate(document_embeddings):
    print(f"Embedding for document {i}: {embedding[:5]} (Length: {len(embedding)})")

# Create the index from the document embeddings
index = VectorStoreIndex.from_documents(documents, show_progress=True)
print(f"Index created of type: {type(index)}")
