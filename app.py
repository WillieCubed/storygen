"""An interactive app.

Running this file is meant to support:
- Gradio/Streamlit
- Other web-based demos

The code pattern to use here is to put all source files in the project folder
and them import exactly what you need here.
"""
from ai_project_template.utils.demo.app import run_demo

if __name__ == '__main__':
    # TODO: Automatically pass command line options
    run_demo()