import gradio as gr
import requests

BACKEND_URL = "http://127.0.0.1:8000"


def upload_pdf(pdf_file):

    with open(pdf_file, "rb") as file:

        response = requests.post(
            f"{BACKEND_URL}/upload",
            files={"file": file}
        )

    return response.json()["message"]


def ask_question(question):

    response = requests.post(
        f"{BACKEND_URL}/ask",
        json={"question": question}
    )

    return response.json()["answer"]


with gr.Blocks(theme=gr.themes.Soft(), 
    css="""
    .gradio-container{
    width:60% !important;
    margin-left:auto !important;
    margin-right:auto !important;
    }
    """
    ) as app:

    gr.Markdown(
        """
        # DocuMind-QA

        Upload a PDF and ask questions about its content.
        """
    )

    with gr.Row():

        pdf_input = gr.File(
            label="Upload PDF",
            file_types=[".pdf"]
        )

    upload_button = gr.Button(
        "Process Document",
        variant="primary"
    )

    upload_status = gr.Textbox(
        label="Status",
        interactive=False
    )

    upload_button.click(
        fn=upload_pdf,
        inputs=pdf_input,
        outputs=upload_status
    )

    gr.Markdown("## Ask Questions")

    question_input = gr.Textbox(
        label="Question",
        placeholder="Type a question about the document"
    )

    ask_button = gr.Button(
        "Get Answer",
        variant="primary"
    )

    answer_output = gr.Textbox(
        label="Answer",
        lines= 4
    )

    ask_button.click(
        fn=ask_question,
        inputs=question_input,
        outputs=answer_output
    )

app.launch()