import gradio as gr
from transformers import pipeline

# Initialize the BART summarization model from Hugging Face
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Define the function that will summarize the text
def summarize_text(input_text, max_length, min_length):
    summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# Example texts for users to try
example_texts = [
    ["The emergence of artificial intelligence (AI) has had a profound impact on many industries, including healthcare, finance, and transportation. AI has enabled automation of complex processes, improving efficiency and reducing costs. However, ethical considerations, such as privacy and job displacement, continue to be points of concern as the technology advances."],
    ["The Great Wall of China, a UNESCO World Heritage site, is one of the most iconic structures in the world. Originally built to protect against invasions, it spans thousands of miles across northern China. Today, the wall attracts millions of tourists each year who come to marvel at its history and grandeur."],
    ["Climate change is one of the most pressing issues of our time. Rising global temperatures, melting ice caps, and extreme weather events are just some of the impacts being observed. Scientists and policymakers are working together to find sustainable solutions to mitigate its effects and protect the planet for future generations."]
]

# Create a Gradio interface
iface = gr.Interface(
    fn=summarize_text,
    inputs=[
        gr.inputs.Textbox(lines=10, label="Enter Text to Summarize", placeholder="Type or paste your article here..."),
        gr.inputs.Slider(50, 200, step=10, default=100, label="Max Length of Summary"),
        gr.inputs.Slider(20, 100, step=10, default=50, label="Min Length of Summary")
    ],
    outputs=gr.outputs.Textbox(label="Summarized Text"),
    title="📄 Text Summarization App",
    description="This app generates a concise summary for long-form text (articles, reports, books, etc.). Adjust the sliders to control the length of the summary. Powered by Hugging Face's BART model.",
    examples=example_texts,
    theme="huggingface",
    live=True,
    allow_flagging="never"
)

# Custom styling for enhanced aesthetics
iface.launch(share=True, server_port=7860, inline=True, 
             server_name="0.0.0.0",
             style={
                "title": {
                    "color": "#5A67D8", 
                    "font-weight": "bold"
                },
                "description": {
                    "color": "#4A5568", 
                    "font-size": "1.1em"
                },
                "input_textbox": {
                    "background-color": "#EDF2F7",
                    "border-radius": "8px",
                    "font-family": "sans-serif"
                },
                "input_slider": {
                    "background-color": "#CBD5E0",
                    "border-radius": "4px"
                },
                "output_textbox": {
                    "background-color": "#E2E8F0",
                    "font-family": "serif"
                },
                "examples": {
                    "background-color": "#E2E8F0",
                    "border-radius": "6px"
                },
                "button": {
                    "background-color": "#4299E1",
                    "color": "#FFF",
                    "font-weight": "bold",
                    "border-radius": "6px"
                }
            }
)
