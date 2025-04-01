![image](https://github.com/user-attachments/assets/be3012ba-e431-4bb6-9c9e-c62c67955a66)


# AI Tutor

This project provides an AI-powered tutoring system designed to assist learners with various subjects.The AI Tutor aims to create an interactive and personalized learning experience. It leverages AI models to answer questions, explain concepts, and provide feedback, making learning more engaging and effective.
It is an application of the Retrieval Augmented Generation (RAG).

![image](https://github.com/user-attachments/assets/2202e42e-9d41-4e87-81e8-d535fc5b36b2)


## Description

**RAG Overview**

RAG combines the power of pre-trained language models (LLMs) with external knowledge sources. The process typically involves:

**Retrieval**:

Fetching relevant information from a knowledge base (like a vector database).
This is where the provided code focuses.

**Augmentation**:

Injecting the retrieved information into the LLM's prompt.

**Generation**:

The LLM generates a response based on the augmented prompt.

## Installation

To know more about the installations, refer to the links below:

Here is the link to client side README.md file - [Client-Side README](client/README.md)

Here is the link to server side README.md file - [Server-Side README](server/README.md)


## Usage

The application has 3 main functionalities for user:

  * **Uploading the file**

  ![image](https://github.com/user-attachments/assets/004978bc-8014-43c5-ba84-aa31a814cc61)


Our user is a student who wants to learn about any topic from the file that they have uploaded.They can upload the file and add certain details like class, subject, chapter name as metadata components. The file data would get stored in the form of chunks in the database.


* **Questions and Answers**

  ![image](https://github.com/user-attachments/assets/66bd8aa5-4d9a-4178-b819-e19cf804e5df)

Students can ask the question related to any topic from that file in two possible ways: Voice Recording and Text. Users can ask any query and they will 
get the best possible response either in text or in voice of the AI Tutor. As per our questions,the retriever will search for closest answers that are stored 
as chunks in the database.


* **Quiz Segment**

  ![image](https://github.com/user-attachments/assets/e13d7f32-cddc-4a9f-a797-55968244f4af)


Now that students have got their answers.They might want to test their knowledge. This is where the third and last functionality comes into play that is a 
quiz. The student will enter the topic and number of questions that they want to answer.






