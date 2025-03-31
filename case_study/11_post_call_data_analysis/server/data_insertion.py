import os
import shutil
from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from config import conn_pinecorn
import time

pc  = conn_pinecorn()
index_name = "dense-index"



#pdf to text function
def to_text(path):
    reader = PdfReader(path)
    text = ""
    for t in reader.pages:
        text =text +" "+ t.extract_text()
    return text

# creating chuks
def create_chunks(chapter_name, class_type, subject,text):
    text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 10000,
    chunk_overlap  = 50
    )
    docs = text_splitter.create_documents([text])
    records = []
    c=0
    for x in docs:
        record = {
            "_id" :str(c),
            "Book"  : subject,
            "Chapter" : chapter_name,
            "Class"  :class_type,
            "page_content":x.page_content,
        }
        c=c+1
        records.append(record)
    return records

# Upsert chunks to the vector DB
def upload_chunks(chunk):
    dense_index = pc.Index(index_name)
    dense_index.upsert_records("example-namespace",chunk)
    time.sleep(10)
    stats = dense_index.describe_index_stats()
    print(stats)

# move file from Raw to Processed and delete it from raw
def move_file(path):
    initial = path
    destination = './Data/Processed'
    shutil.move(initial,destination)

    
# function to insert the pdf into vector DB
def insert_data(path,chapter_name, class_type, subject):
    pc  = conn_pinecorn()
    index_name = "dense-index"
    if not pc.has_index(index_name):
        pc.create_index_for_model(
            name=index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"llama-text-embed-v2",
                "field_map":{"text": "page_content"}
            }
        )
    
    pdf_text = to_text(path)
    chunks = create_chunks(chapter_name, class_type, subject,pdf_text)
    upload_chunks(chunks)
    return(chunks)
