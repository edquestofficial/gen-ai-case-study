from llama_index.core import SimpleDirectoryReader, VectorStoreIndex  # Importing the necessary classes for reading documents and creating a vector index
from llama_index.embeddings.huggingface import HuggingFaceEmbedding  # Importing the class for generating embeddings using a Hugging Face model
from llama_index.core import Settings, StorageContext  # Importing settings and storage context for configuring the embedding model and vector store
from llama_index.llms.gemini import Gemini  # Importing the Gemini LLM for generating responses
from llama_index.vector_stores.redis import RedisVectorStore  # Importing the Redis vector store for storing embeddings
from dotenv import load_dotenv  # Importing to load environment variables from a .env file
import os  # Importing the os module to access environment variables
import redis  # Importing the Redis library for connecting to the Redis server

def main():
    load_dotenv()  # Load environment variables from the .env file

    # Initialize the Redis client with credentials from environment variables
    redis_client = redis.Redis(host='localhost', port=6379, username=os.getenv("REDIS_USERNAME"), password=os.getenv("REDIS_PASSWORD"))

    try:
        redis_client.ping()  # Ping the Redis server to check the connection
        print("Connected to Redis successfully!")
    except:
        print("Error connecting to Redis")  # Handle connection errors

    # Load documents from the specified directory with parallel processing
    documents = SimpleDirectoryReader(input_dir='./data').load_data(num_workers=4)
    
    # Print the number of loaded documents
    length = len(documents)
    print(f"Loaded {length} documents")

    # Configure the embedding model and LLM settings
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    Settings.llm = Gemini(api_key=os.getenv("GEMINI_API_KEY"), model="models/gemini-pro")

    # Initialize the Redis vector store and storage context
    vector_store = RedisVectorStore(redis_client=redis_client, overwrite=True)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Create the index from the document embeddings with progress display
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context, show_progress=True)

if __name__ == "__main__":
    main()  # Run the main function
