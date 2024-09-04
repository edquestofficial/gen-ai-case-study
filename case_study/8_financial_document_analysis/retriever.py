from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, StorageContext
from llama_index.llms.gemini import Gemini
from llama_index.vector_stores.redis import RedisVectorStore
from dotenv import load_dotenv
import os
import redis
from redisvl.schema import IndexSchema

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

    schema = IndexSchema.from_dict({
      "index": {"name": "data", "prefix": "docs"},
      "fields": [
        {"name": "id", "type": "tag"},
        {"name": "doc_id", "type": "tag"},
        {"name": "text", "type": "text"},
        {"name": "vector", "type": "vector", "attrs": {"dims": 384, "algorithm": "flat"}}
      ]
    })

    vector_store = RedisVectorStore(schema=schema,redis_client=redis_client)

    # Configure the embedding model and LLM settings
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    Settings.llm = Gemini(api_key=os.getenv("GEMINI_API_KEY"), model="models/gemini-pro")

    # # Initialize the Redis vector store and storage context
    # storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Create the index from the document embeddings with progress display
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    
    query = input(str("Enter your query: "))
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print(response)
             
if __name__ == "__main__":
    main()  # Run the main function