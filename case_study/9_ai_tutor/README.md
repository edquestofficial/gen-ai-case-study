**This is the Server-side Readme.md file for AI Tutor**

## Prerequisites

 Python 3.13.2

 Pincone
 
 Google gen-ai
 
 langchain
 
 pypdf

For more information, refer to the `requirements.txt` file.


## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/edquestofficial/ai-tutor.git]
    ```



2.  **Install dependencies:**

    * This project mainly uses Python on the server side.

      Go to the official Python website: python.org.

      After installation of python, verify by giving the following command in command prompt:

    ```bash
    python --version
    ```

    * Created a virtual environment and activated it using the following commands
  
    ```bash
    python -m venv venv
    venv/Scripts/activate
    ```

    * Consult the project's `requirements.txt` for dependencies and install them using pip:

        ```bash
        pip install -r requirements.txt
        ```


3.  **Set up API keys for AI model and Vector Database:**

    * The AI Tutor requires API keys for Gemini. Users can create their own API keys from Google Studio.

    * Pinecone Vector Database has been used as a database to store the data and give results when fetched according to the requirements. Users can create their own API keys from Pinecone.



4. **Environment Variables:**

The following environment variables are used for accessing the vector database as Pinecone and an AI model as Gemini:

 * `GEMINI_API_KEY`: Your API key (required).
 * `PINECONE_API_KEY`: Your API key (required).

 To set environment variables, create a `.env` file in the project.

5. **To Start Backend Server :-**

Once you have created virtual environment and installed all libraries and dependencies, run below command to start the server - 

```sh

fastapi dev src/app.py
```


