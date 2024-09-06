from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, QueryBundle
from llama_index.llms.gemini import Gemini
from llama_index.vector_stores.redis import RedisVectorStore
from dotenv import load_dotenv
import os
import redis
from redisvl.schema import IndexSchema
from llama_index.llms.gemini import Gemini


def create_semantic_query(query):
  # create a QueryBundle object from the query string
  query_bundle = QueryBundle(query)
  # retrieve top 5 most similar documents
  retriever = index.as_retriever(similarity_top_k=5)
  retrieved_nodes = retriever.retrieve(query_bundle)

  return retrieved_nodes

def query_semantic_data(initial_query):
    retrieved_nodes = create_semantic_query(initial_query)
    response_text = [node.node.get_text() for node in retrieved_nodes]

    #Combine the response and pass through the LLM to generate a response
    context= "\n\n\n".join(response_text)
    prompt = f"You are a financial data analyzer chatbot. You have to search for the answer of the query from the given context. Remember, don't use your own knowledge for finding answers. The context is the following: {context} \n, the query is: {initial_query}"
    # generate the generative response from the llm
    resp = llm.complete(prompt)
    print('Generative Response from LLM')
    print(resp)

def main():   
    query = input(str("Enter your query: "))
    query_engine = index.as_query_engine()  # Create a query engine from the index
    response = query_engine.query(query)  # Query the index with the user's query
    print('response from query_engine')
    print(response)
    query_semantic_data(query)  # Call the function to query semantic data


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from the .env file

    # Initialize the Redis client with credentials from environment variables
    redis_client = redis.Redis(host='localhost', port=6379, username=os.getenv("REDIS_USERNAME"), password=os.getenv("REDIS_PASSWORD"))

    try:
        redis_client.ping()  # Ping the Redis server to check the connection
        print("Connected to Redis successfully!")
    except:
        print("Error connecting to Redis")  # Handle connection errors

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
    llm = Gemini(api_key=os.getenv("GEMINI_API_KEY"), model="models/gemini-1.5-pro")
    Settings.llm = llm

    # Create the index from the document embeddings with progress display
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

    main()  # Run the main function
