import gradio as gr


def run_demo(web_title='An AI Project'):
    """Run a web demo of this AI app.
    
    This is the primary entrypoint to this project's web demo using Gradio.
    """
    with gr.Blocks(title=web_title) as demo:
        # Placeholder
        gr.Markdown(f'# {web_title} demo.')
        gr.Markdown('Show me something cool!')
    demo.launch()