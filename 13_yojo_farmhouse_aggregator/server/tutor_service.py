from config import conn_pinecorn, conn_gemini

class TutorService():
    index_name = "dense-index"

    def __semantic_search(self, question):
        pc = conn_pinecorn()
        dense_index = pc.Index(self.index_name)
        results = dense_index.search(
            namespace="python_book",
            query={
                "top_k": 5,
                "inputs": {'text': question},
                "filter": {"book_name": "let us python"}
            }
        )
        return results
    
    def __get_prompt(self, question, context):
        prompt = f"""
        You are a highly professional science teacher of class 9th.

        
        1. Provide a clear and detailed beginner-friendly explanation of the logic and structure of the code or concept.
        2. Focus on helping the user understand the underlying logic and how the code works.
        3. Keep the response concise (within **5 sentences**) and easy to follow.
        4. Avoid unnecessary complexity and use simple terms where possible.

        
        **Question:** {question}  
        **Context:** {context}

        
        - Provide a detailed explanation of the code or concept.
        - Focus on clarity and accuracy.
        """
        return prompt

    def __get_quiz_prompt(self, question, context, number):
        format = [{
            "id": "question-id",
            "question": "Sample question",
            "options": ["option1", "option2", "option3", "option4"],
            "correct_answer": "answer"
        }]
        
        prompt = f"""
        You are a highly professional science teacher of class 9th.

        
        1. To generate multiple-choice questions (MCQ) related to the provided context.
        2. Follow the format strictly and provide a **valid JSON object** only.
        3. Ensure the options are logically consistent and relevant to the question.
        4. Provide {number} questions (MCQ).

        
        ```json
        {format}
        """
        return prompt

    def __get_context(self, chunks):
        llmtext = ""
        for hit in chunks['result']['hits']:
            llmtext = llmtext + " " + hit['fields']['chunk_text']
        return llmtext
    
    def __execute_prompt(self, prompt):
        client = conn_gemini()
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        print(response.text)
        return response.text
    
    def get_question_answer(self, question):
        semantic_result = self.__semantic_search(question)
        context = self.__get_context(semantic_result)
        prompt = self.__get_prompt(question, context)
        response = self.__execute_prompt(prompt)
        return response
    
    def get_quiz(self, question, number):
        semantic_result = self.__semantic_search(question)
        context = self.__get_context(semantic_result)
        prompt = self.__get_quiz_prompt(question, context, number)
        response = self.__execute_prompt(prompt)
        return response
    
