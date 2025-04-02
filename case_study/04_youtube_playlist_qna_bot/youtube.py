import gradio as gr
from Links_Generator import get_playlist_items
from Transcript_Generator import generate_Transcript
from generator import generate_embeddings
from retriever import generate_answers
import whisper
import time

whisper_model = whisper.load_model("base")

# Function to process YouTube playlist and generate transcripts
def process_playlist(url):
    links = get_playlist_items(url)

    transcripts = []
    num_videos = len(links)
    
    # Create a progress tracker instance
    progress_tracker = gr.Progress(num_videos)
    
    for i, link in enumerate(links, start=1):
        transcript = generate_Transcript(link)
        transcripts.append(f"Video {i}:\n {transcript}")
        generate_embeddings(transcript)
        # Update progress
        progress_tracker.update(i)
        time.sleep(1)

    return "Processing Completed."

# Function to generate answers from text input
def generate_text_answer(question):
    if question.lower() == "exit":
        return "Session terminated."

    answer = generate_answers(question)
    return answer

# Function to generate answers from voice input
def generate_voice_answer(audio):
    # Load the audio file
    audio_file = whisper.load_audio(audio)
    result = whisper_model.transcribe(audio_file, verbose=True)
    question = result["text"]

    if question.lower() == "exit":
        return "Session terminated."

    answer = generate_answers(question.lower())
    return answer

# Gradio interface
def gradio_interface():
    with gr.Blocks(theme=gr.themes.Default(primary_hue=gr.themes.colors.red, secondary_hue=gr.themes.colors.pink)) as demo:
        with gr.Row():
            gr.Image(value="./utils/logo.jpeg", label="YouTube QnA Bot", type="filepath", scale=1)
            gr.Label("YouTube QnA Bot", scale=4)

        with gr.Row():
            url_input = gr.Textbox(label="Enter YouTube playlist URL", placeholder="YouTube playlist URL")
            process_button = gr.Button("Process Playlist", variant="primary")
        
        # Add a progress bar and status output
        progress_tracker = gr.Progress()
        status_output = gr.Textbox(label="Status", placeholder="Processing status will appear here", lines=2)

        # Define the function that updates the progress
        def update_progress(url):
            status = process_playlist(url)
            return status

        process_button.click(fn=update_progress, inputs=url_input, outputs=status_output)

        with gr.Row():
            answer_output = gr.Textbox(label="Answer", placeholder="Answer will appear here", lines=5)
      
        with gr.Row():
            audio_input = gr.Audio(sources="microphone", type="filepath", scale=4)
            ask_voice_button = gr.Button("Ask (Voice)", scale=1, variant="primary")

        with gr.Row():
            question_text_input = gr.Textbox(label="Enter your question", placeholder="Ask your question here", scale=4)
            ask_text_button = gr.Button("Ask (Text)", scale=1, variant="primary")
        
        ask_text_button.click(generate_text_answer, inputs=question_text_input, outputs=answer_output)
        ask_voice_button.click(generate_voice_answer, inputs=audio_input, outputs=answer_output)

    return demo

# Launch the Gradio interface
gradio_interface().launch(share=True)
