from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv
import os
import redis
import io



def main():
  load_dotenv()

  r= redis.Redis(host='localhost', port=6379, username=os.getenv("REDIS_USERNAME"), password=os.getenv("REDIS_PASSWORD"))

  try:
    r.ping()
    print("Connected to Redis successfully!")
  except redis.ConnectionError as e:
    print(f"Error connecting to Redis: {e}")

  documents = SimpleDirectoryReader(input_dir='./data').load_data(num_workers=4)
  
  # Print document details
  length = len(documents)
  print(f"Loaded {length} documents")
  
  embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5", embed_batch_size=20)

  Settings.embed_model = embed_model
  Settings.llm = Gemini(api_key=os.getenv("GEMINI_API_KEY"), model="models/gemini-pro")

  document_embeddings = [embed_model.get_text_embedding(doc.get_text()) for doc in documents]

  # Create the index from the document embeddings
  index = VectorStoreIndex.from_documents(documents, show_progress=True)
  print(f"Index created of type: {type(index)}")

if __name__ == "__main__":
    main()