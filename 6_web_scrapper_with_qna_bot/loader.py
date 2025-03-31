from bs4 import BeautifulSoup
from llama_index.llms.gemini import Gemini
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from IPython.display import Markdown, display
import chromadb

# Use the dir path of local system where data stored
documents = SimpleDirectoryReader("").load_data()

print(len(documents))

api_key = os.getenv("GEMINI_API_KEY")
llm = Gemini(api_key=api_key, model_name="models/gemini-pro")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Use the dir path of local system where want to stored the data in chroma db, ex: dir name "chroma_db"
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)