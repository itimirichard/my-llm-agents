import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)

async def run(query: str):
    async for status in ResearchManager().run(query):
        yield status

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky", secondary_hue="gray")) as demo:
    gr.Markdown("# Deep Research")
    query_input = gr.Textbox(label="What topic do you want to research?")
    report = gr.Markdown(label="Report")
    run_button = gr.Button("Run Research", variant="primary")

    run_button.click(run, inputs=[query_input], outputs=[report])
    # When the user presses Enter in the query input, run the research
    query_input.submit(run, inputs=[query_input], outputs=[report])

demo.launch(inbrowser=True)