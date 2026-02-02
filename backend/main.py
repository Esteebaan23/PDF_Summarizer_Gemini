import gradio as gr
from fastapi import FastAPI
from backend.services import RAGService

app = FastAPI()
rag_service = RAGService()

# Función para la lógica del chat
def chat_response(message, history):
    # message es la pregunta actual, history son los mensajes previos
    response = rag_service.get_answer(message)
    return response

# Función para procesar el archivo (se mantiene aparte)
def upload_file(file):
    if file:
        return rag_service.process_pdf(file.name)
    return "No se cargó archivo."

# Diseño de la Interfaz tipo Chat
with gr.Blocks(theme=gr.themes.Soft(), title="Harold AI Chat") as demo:
    gr.Markdown("# 🤖 RAG Analyzer Pro")
    
    with gr.Row():
        with gr.Column(scale=1):
            file_output = gr.File(label="1. Sube tu Documento")
            status = gr.Textbox(label="Estado", interactive=False)
            file_output.change(upload_file, inputs=file_output, outputs=status)
            
        with gr.Column(scale=3):
            # El componente de Chat se encarga de todo el historial
            chat_ui = gr.ChatInterface(
                fn=chat_response,
                examples=["¿Qué dice este documento?", "Resume los puntos clave"],
                title="Conversa con tu PDF"
            )

app = gr.mount_gradio_app(app, demo, path="/")