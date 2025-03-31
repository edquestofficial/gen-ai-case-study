from llama_index.core import QueryBundle

def create_semantic_query(query,index):
    # Create a QueryBundle object from the query string, which packages the query for retrieval
    query_bundle = QueryBundle(query)
    # Use the index to retrieve the top 5 most similar documents based on similarity search
    retriever = index.as_retriever(similarity_top_k=5)
    retrieved_nodes = retriever.retrieve(query_bundle)

    return retrieved_nodes

def query_semantic_data(initial_query,llm,index):
    # Retrieve the most similar documents related to the initial query
    retrieved_nodes = create_semantic_query(initial_query, index)
    # Extract the text from the retrieved nodes (documents)
    response_text = [node.node.get_text() for node in retrieved_nodes]

    # Combine the retrieved texts into a single context and create a prompt for the LLM
    context = "\n\n\n".join(response_text)
    prompt = (f"You are initially a financial data analyzer chatbot. You have to search for the answer of the query from the given context. Remember, don't use your own knowledge for finding answers. The context is the following: {context} \n, the query is: {initial_query}  ### If you doesn't find relevant answer from the context.try to search it on web and give answer by specifying that you find this answer from web")
    
    # Generate a response using the language model (LLM) with the provided prompt
    response = llm.complete(prompt)
    
    return response
