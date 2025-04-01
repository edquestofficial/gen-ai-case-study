# AI Tutor

This project provides an AI-powered tutoring system designed to assist learners with various subjects.

## Description

The AI Tutor aims to create an interactive and personalized learning experience. It leverages AI models to answer questions, explain concepts, and provide feedback, making learning more engaging and effective.
It is an application of the Retrieval Augmented Generation (RAG) pipeline, specifically the retrieval part. Here's a breakdown:

RAG Overview

RAG combines the power of pre-trained language models (LLMs) with external knowledge sources. The process typically involves:

Retrieval:
Fetching relevant information from a knowledge base (like a vector database).
This is where the provided code focuses.

Augmentation:
Injecting the retrieved information into the LLM's prompt.

Generation:
The LLM generates a response based on the augmented prompt.

## Installation

To know more about the installations, refer to the links below:

Here is the link to client side README.md file - [Client-Side README](client/README.md)

Here is the link to server side README.md file - [Server-Side README](server/README.md)


## Usage

The application has 3 main functionalities for user:

  * **Inserting the Data and Metadata (Uploading the file)**

Our user is a student who wants to learn about any topic from the file that they have uploaded.
They can upload the file and add certain details like class, subject, chapter name as metadata components. The file data would get stored in the form of chunks in the database.


*Get Responses in form of Chunks (Questions and Answers)

Now, students can ask the question related to any topic from that file in two possible ways: Voice Recording and Text. Users can ask any query and they will get the best possible response either in text or in voice of the AI Tutor. As per our questions,the retriever will search for closest answers that are stored as chunks in the database.


*Another Implementation of Chunking

Now that students have got their answers.They might want to test their knowledge. This is where the third and last functionality comes into play that is a quiz. The student will enter the topic and number of questions that they want to answer.






