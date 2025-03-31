from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.llms.gemini import Gemini
from llama_index.vector_stores.redis import RedisVectorStore
from dotenv import load_dotenv
import os
import redis
from redisvl.schema import IndexSchema

def initialize_vector_store():
    load_dotenv()
    redis_client = redis.Redis(
        host='localhost', 
        port=6379, 
        username=os.getenv("REDIS_USERNAME"), 
        password=os.getenv("REDIS_PASSWORD")
    )
    try:
        redis_client.ping()
        print("Connected to Redis successfully!")
    except:
        print("Error connecting to Redis")
        return None

    schema = IndexSchema.from_dict({
        "index": {"name": "data", "prefix": "docs"},
        "fields": [
            {"name": "id", "type": "tag"},
            {"name": "doc_id", "type": "tag"},
            {"name": "text", "type": "text"},
            {"name": "vector", "type": "vector", "attrs": {"dims": 384, "algorithm": "flat"}}
        ]
    })
    vector_store = RedisVectorStore(schema, redis_client)
    return vector_store

def initialize_cache_store():
    load_dotenv()
    redis_client = redis.Redis(
        host='localhost', 
        port=6379, 
        username=os.getenv("REDIS_USERNAME"), 
        password=os.getenv("REDIS_PASSWORD")
    )
    try:
        redis_client.ping()
        print("Connected to Redis Cache Database successfully!")
    except:
        print("Error connecting to Cache Database")
        return None

    schema = IndexSchema.from_dict({
    "index": {
        "name": "cache_data", 
        "prefix": "cache",
        "storage_type": "hash",
    },
    "fields": [
            {"name": "id", "type": "tag"},
            {"name": "doc_id", "type": "tag"},
            {"name": "text", "type": "text"},
            {"name": "updated_at", "type": "numeric"},
            {"name": "vector", "type": "vector", "attrs": {"dims": 384, "algorithm": "flat",}}
        ]
    })

    vector_store = RedisVectorStore(schema, redis_client)
    return vector_store

def initialize_llm():
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    llm = Gemini(api_key=os.getenv("GEMINI_API_KEY"), model="models/gemini-1.5-pro")
    Settings.llm = llm
    return llm