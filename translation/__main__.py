import gradio as gr

from translation import translate_en, translate_ja

with gr.Blocks() as app:
    with gr.Tab(label="English to Japanese"):
        ej_input_text = gr.Textbox(lines=5, label="Input Text")
        ej_output_text = gr.Textbox(lines=5, label="Output Text")
        ej_button = gr.Button(label="Translate")
    with gr.Tab(label="Japanese to English"):
        ja_input_text = gr.Textbox(lines=5, label="Input Text")
        ja_output_text = gr.Textbox(lines=5, label="Output Text")
        ja_button = gr.Button(label="Translate")
    ej_button.click(translate_en, inputs=ej_input_text, outputs=ej_output_text)
    ja_button.click(translate_ja, inputs=ja_input_text, outputs=ja_output_text)

app.launch()
