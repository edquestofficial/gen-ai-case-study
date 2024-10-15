import nest_asyncio
import logging
import sys
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.postprocessor import LLMRerank
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core import QueryBundle
import pandas as pd
from IPython.display import display, HTML

# Apply Nest Asyncio
nest_asyncio.apply()

# Configure Logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

class Reranking:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Reranking, cls).__new__(cls)
            cls._instance.initialize(*args, **kwargs)
        return cls._instance

    def initialize(self, data_directory: str, api_key: str, embed_model: str = "BAAI/bge-base-en-v1.5", model_name: str = "models/gemini-1.5-pro"):
        # Settings for embedding model and LLM
        Settings.embed_model = HuggingFaceEmbedding(model_name=embed_model)
        Settings.llm = Gemini(api_key=api_key, temperature=0, model=model_name)
        Settings.chunk_size = 512

        # Load documents from the provided directory
        self.documents = SimpleDirectoryReader(data_directory).load_data()

        # Build VectorStoreIndex
        self.index = VectorStoreIndex.from_documents(self.documents)

    def get_retrieved_nodes(self, query_str: str, vector_top_k=10, reranker_top_n=3, with_reranker=False):
        query_bundle = QueryBundle(query_str)
        
        # Configure retriever
        retriever = VectorIndexRetriever(index=self.index, similarity_top_k=vector_top_k)
        retrieved_nodes = retriever.retrieve(query_bundle)

        if with_reranker:
            # Configure reranker
            reranker = LLMRerank(choice_batch_size=5, top_n=reranker_top_n)
            retrieved_nodes = reranker.postprocess_nodes(retrieved_nodes, query_bundle)

        return retrieved_nodes

    def visualize_retrieved_nodes(self, nodes) -> None:
        result_dicts = []
        for node in nodes:
            result_dict = {"Score": node.score, "Text": node.node.get_text()}
            result_dicts.append(result_dict)
        self.pretty_print(pd.DataFrame(result_dicts))

    @staticmethod
    def pretty_print(df):
        return display(HTML(df.to_html().replace("\\n", "")))

    def query_engine_response(self, query_str: str, similarity_top_k=3, reranker_top_n=2):
        query_engine = self.index.as_query_engine(
            similarity_top_k=similarity_top_k,
            node_postprocessors=[
                LLMRerank(choice_batch_size=5, top_n=reranker_top_n)
            ],
            response_mode="tree_summarize",
        )
        return query_engine.query(query_str)
