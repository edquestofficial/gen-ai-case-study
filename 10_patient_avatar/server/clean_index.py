from config import conn_pinecorn


pc= conn_pinecorn()
def clean():
    pc.delete_index("dense-index")

clean()