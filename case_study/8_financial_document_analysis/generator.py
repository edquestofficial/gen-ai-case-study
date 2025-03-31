from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import StorageContext
from dotenv import load_dotenv
from initialization import initialize_vector_store, initialize_llm

def generate_embeddings(path):
    
    vector_store = initialize_vector_store()

    # Configure the embedding model and LLM settings
    initialize_llm()

    # Initialize the Redis vector store and storage context
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Load documents from the specified directory with parallel processing
    documents = SimpleDirectoryReader(input_dir=path).load_data(num_workers=4)
    
    # Print the number of loaded documents
    length = len(documents)
    print(f"Loaded {length} documents")

    # Create the index from the document embeddings with progress display
    try:
      index = VectorStoreIndex.from_documents(documents, storage_context=storage_context, show_progress=True)
      print("Index created successfully!")
      return True
    except:
      return False        