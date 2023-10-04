import gradio as gr
import os
from gpt_author_v2 import create_fantasy_novel

# Simplified function, replace with actual functionality from notebook
def write_fantasy_novel(prompt, num_chapters, writing_style, claude_true=False):
    # Replace this function with actual functionality from the notebook
    novel = f"Sample Novel based on:\nPrompt: {prompt}\nNum Chapters: {num_chapters}\nWriting Style: {writing_style}\n"
    title = "Sample Title"
    chapters = ["Sample Chapter 1", "Sample Chapter 2"]
    chapter_titles = ["Chapter 1 - Title", "Chapter 2 - Title"]
    return novel, title, chapters, chapter_titles

# Function to be used in Gradio UI
def generate_and_save_novel(prompt, num_chapters, writing_style, extra_guideline, plot_design, world_building, character_depth):
    title = create_fantasy_novel(prompt, num_chapters, writing_style, extra_guideline, plot_design, world_building, character_depth)
    file_path = f"content/{title}.epub"
    return file_path

# Gradio UI
def gradio_ui():
    iface = gr.Interface(
        fn=generate_and_save_novel, 
        inputs=[
            gr.inputs.Textbox(lines=3, label="Prompt"),
            gr.inputs.Slider(minimum=1, maximum=100, default=15, label="Number of Chapters"),
            gr.inputs.Textbox(lines=3, label="Writing Style"),
            gr.inputs.Textbox(lines=3, label="Extra Guideline"),
            gr.inputs.Textbox(lines=3, label="Plot Design"),
            gr.inputs.Textbox(lines=3, label="World Building"),
            gr.inputs.Textbox(lines=3, label="Character Depth")
        ],
        outputs=gr.outputs.File(label="Download Generated Novel"),
        live=False, # This means the function will only be called when the user presses the "Submit" button
        submit_button_name="Generate"
    )
    iface.launch()

# Run the Gradio UI
gradio_ui()