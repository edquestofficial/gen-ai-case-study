from llama_index.readers.youtube_transcript import YoutubeTranscriptReader

def generate_Transcript(url):
    url = url
    loader = YoutubeTranscriptReader()
    documents = loader.load_data(
      ytlinks= [url]
    )
    return documents
    