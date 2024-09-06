from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, QueryBundle
from llama_index.llms.gemini import Gemini
from llama_index.vector_stores.redis import RedisVectorStore
from dotenv import load_dotenv
import os
import redis
from redisvl.schema import IndexSchema

def create_semantic_query(query):
    # Create a QueryBundle object from the query string, which packages the query for retrieval
    query_bundle = QueryBundle(query)
    # Use the index to retrieve the top 5 most similar documents based on similarity search
    retriever = index.as_retriever(similarity_top_k=5)
    retrieved_nodes = retriever.retrieve(query_bundle)

    return retrieved_nodes

def query_semantic_data(initial_query):
    # Retrieve the most similar documents related to the initial query
    retrieved_nodes = create_semantic_query(initial_query)
    # Extract the text from the retrieved nodes (documents)
    response_text = [node.node.get_text() for node in retrieved_nodes]

    # Combine the retrieved texts into a single context and create a prompt for the LLM
    context = "\n\n\n".join(response_text)
    prompt = (f"You are a financial data analyzer chatbot. You have to search for the answer of the query from the given context. Remember, don't use your own knowledge for finding answers. The context is the following: {context} \n, the query is: {initial_query}")
    
    # Generate a response using the language model (LLM) with the provided prompt
    resp = llm.complete(prompt)
    print('Generative Response from LLM')
    print(resp)

def main():   
    # Get the user's query input
    query = input(str("Enter your query: "))
    
    # Create a query engine from the index and query it with the user's query
    query_engine = index.as_query_engine()  
    response = query_engine.query(query)  # Fetch the response from the index
    print('Response from query_engine')
    print(response)
    
    # Call the function to query the semantic data and retrieve relevant documents
    query_semantic_data(query)  

if __name__ == "__main__":
    # Load environment variables (e.g., Redis credentials, API keys) from a .env file
    load_dotenv()

    # Initialize Redis client with the credentials loaded from the environment variables
    redis_client = redis.Redis(
        host='localhost', 
        port=6379, 
        username=os.getenv("REDIS_USERNAME"), 
        password=os.getenv("REDIS_PASSWORD")
    )

    try:
        # Ping the Redis server to check if the connection is successful
        redis_client.ping()
        print("Connected to Redis successfully!")
    except:
        print("Error connecting to Redis")  # Handle errors if Redis connection fails

    # Define the schema for the Redis vector store, specifying the fields and vector configuration
    schema = IndexSchema.from_dict({
        "index": {"name": "data", "prefix": "docs"},
        "fields": [
            {"name": "id", "type": "tag"},
            {"name": "doc_id", "type": "tag"},
            {"name": "text", "type": "text"},
            {"name": "vector", "type": "vector", "attrs": {"dims": 384, "algorithm": "flat"}}
        ]
    })

    # Create a Redis-based vector store to store document embeddings
    vector_store = RedisVectorStore(schema=schema, redis_client=redis_client)

    # Configure the embedding model using HuggingFace and set up the language model (LLM) using Gemini
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    llm = Gemini(api_key=os.getenv("GEMINI_API_KEY"), model="models/gemini-1.5-pro")
    Settings.llm = llm

    # Create the document index from the vector store that holds the document embeddings
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

    # Run the main function, which handles user input and queries
    main()
