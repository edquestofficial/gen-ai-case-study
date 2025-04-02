from llama_index.core import VectorStoreIndex
from caching import get_cached_response, cache_response
from retriever import query_semantic_data
from initialization import initialize_llm, initialize_vector_store

# Initialize the vector store
vector_store = initialize_vector_store()
# Initialize LLM
llm = initialize_llm()
# Create the index
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

def run_query(query):   
    cached_response = get_cached_response(query)
    if cached_response is None:
        response = query_semantic_data(initial_query=query, llm=llm, index=index)
        cache_response(user_query=query, response=response)
        print("Cache not present!")
        return response
    else:
        print("Cache hit!")
        return cached_response