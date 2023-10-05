import gradio as gr
import os
from gpt_author_v2 import create_fantasy_novel

INPUT_GUIDANCE = {
    'prompt': "Enter a brief scenario, question, or concept that encapsulates the primary idea or situation your novel will explore. This could be a conflict, a mystery, a setting, or a character's predicament.",
    'writing_style': "Describe the writing style for your novel. Consider aspects like sentence structure, tone, and lexicon. Examples might include 'concise and to-the-point', 'flowery and descriptive', or 'casual and conversational'.",
    'extra_guideline': "Include any additional instructions, preferences, or guidelines that are pertinent to the writing of your novel. This could encompass specific do's or don'ts, thematic considerations, or particular elements to include or avoid.",
    'plot_design': "Outline the main events and turning points in your novel. Consider how conflicts will arise and be resolved, and how the story will progress from beginning to end.",
    'world_building': "Describe the setting of your novel, including the physical environment, cultures, and social norms. Consider how the world's unique characteristics will impact the story and character development.",
    'character_depth': "Detail the main characters of your novel, including their backgrounds, motivations, and development arcs. Consider how their individual stories will intersect with and drive the overall plot."
}

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
            gr.inputs.Textbox(lines=3, label="Prompt", placeholder=INPUT_GUIDANCE['prompt']),
            gr.inputs.Slider(minimum=1, maximum=100, default=15, label="Number of Chapters"),
            gr.inputs.Textbox(lines=3, label="Writing Style", placeholder=INPUT_GUIDANCE['writing_style']),
            gr.inputs.Textbox(lines=3, label="Extra Guideline", placeholder=INPUT_GUIDANCE['extra_guideline'], optional=True),
            gr.inputs.Textbox(lines=3, label="Plot Design", placeholder=INPUT_GUIDANCE['plot_design'], optional=True),
            gr.inputs.Textbox(lines=3, label="World Building", placeholder=INPUT_GUIDANCE['world_building'], optional=True),
            gr.inputs.Textbox(lines=3, label="Character Depth", placeholder=INPUT_GUIDANCE['character_depth'], optional=True)
        ],
        outputs=gr.outputs.File(label="Download Generated Novel"),
        live=False, # This means the function will only be called when the user presses the "Submit" button
    )
    iface.launch()

# Run the Gradio UI
gradio_ui()