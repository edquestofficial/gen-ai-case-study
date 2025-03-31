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

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/edquestofficial/ai-tutor.git](https://github.com/edquestofficial/ai-tutor.git)
    cd ai-tutor
    ```

2.  **Install dependencies:**

    * This project likely uses Python and requires specific libraries.
    * Created a virtual environment and activated it using the following commands

    ```bash
    python -m venv venv
    venv/Scripts/activate
    source venv/bin/activate

    * Consult the project's `requirements.txt` for dependencies and install them using pip:

        ```bash
        pip install -r requirements.txt
        ```

3.  **Set up API keys :**

    * The AI Tutor requires API keys for Gemini services. Created an API key for Gemini from Google Studio and used it in the project.
      

4.  **Database setup:**

    * Pinecone Vector database has been used to store the data and give results when fetched according to the requirements.

## Usage

1.  **Run the application:**

    * Execute the main script of the AI Tutor. For example, if the main script is `main.py`:

        ```bash
        python main.py
        ```

2.  **Interact with the tutor:**

   

3.  **Configuration:**

    * Refer to the project's configuration files or documentation to customize settings like the AI model, learning parameters, or user preferences.


## Acknowledgments

* [Mention any libraries or resources used, e.g., OpenAI, specific frameworks]
* [Acknowledge any contributors or individuals who helped with the project]

