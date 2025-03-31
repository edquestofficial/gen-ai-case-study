from config import conn_pinecorn, conn_gemini

pc = conn_pinecorn()
client = conn_gemini()

index_name = "dense-index"
query = "What is JVM?"
def LLMresponse():
    dense_index = pc.Index(index_name)
    results = dense_index.search(
        namespace="example-namespace", 
        query={
            "inputs": {"text": query}, 
            "top_k": 2
        },
       
    )
    llmtext = ""
    if not results['result']['hits']:
        print("No matching records found in Pinecone.")
    else:
        llmtext = ""
        for hit in results['result']['hits']:
            print(f"id: {hit['_id']}, score: {round(hit['_score'],2)}, text: {hit['fields']['chunk_text']}")
            llmtext += hit['fields']['chunk_text'] + " "
        print("---------------------------------------------------")
    print(llmtext)


    # prompt = f"""
    # You are an experienced Java developer with deep knowledge of object-oriented programming, design patterns, and best practices. 
    # Provide clear, detailed, and beginner-friendly explanations, focusing on helping the user understand the logic and structure of the code.  If asked for MCQs, you have to provide 4 options, and a correct answer.
    # question : {query} \n
    # context : {llmtext}
    # """

    # response = client.models.generate_content(
    #         model="gemini-2.0-flash", contents=prompt
    #     )

    # return response.text

print(LLMresponse())



