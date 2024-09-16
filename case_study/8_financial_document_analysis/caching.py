import os
from llama_index.core import VectorStoreIndex, StorageContext, SimpleDirectoryReader
from initialization import initialize_cache_store, initialize_llm

# Initialize Redis client
vector_store = initialize_cache_store()

# Initialize LLM
initialize_llm()   

def creating_cache(query,response):
    # Specify the folder path and file name
    folder_path = 'cache_data'
    file_name = 'data.txt'
    file_path = os.path.join(folder_path, file_name)

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    data = f""""query": {query},
"response": {response}
"""
    # Open the file in the specified folder and write to it
    with open(file_path, 'w') as file:
        file.write(data)

def get_cached_response(user_query):
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

    # Create the index
    retriever = index.as_retriever(similarity_top_k=1)
    result_nodes = retriever.retrieve(user_query)
    score = result_nodes[0].score
    cached_response = result_nodes[0].text

    if score > 0.7:
        # Return the cached response
        return cached_response
    else:
        return None
    
def cache_response(user_query, response):
    """Store the query and response in the Redis cache."""
    creating_cache(user_query, response)
    # Create the index
    documents = SimpleDirectoryReader(input_files=['cache_data/data.txt']).load_data()

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    index=VectorStoreIndex.from_documents(documents, storage_context=storage_context,show_progress=True)
    print("cache stored successfully")