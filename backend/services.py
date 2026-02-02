from langchain_google_vertexai import VertexAI, VertexAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from config.settings import settings

class RAGService:
    def __init__(self):
        # Forzamos los argumentos con nombre para evitar errores de asignación
        self.llm = VertexAI(
            model_name=settings.MODEL_NAME, # gemini-1.5-flash
            project=settings.PROJECT_ID,    # Tu ID real de GCP
            location=settings.LOCATION,     # us-central1
            max_output_tokens=1024,
            temperature=0.1
        )
        
        # IMPORTANTE: Los embeddings también necesitan location
        self.embeddings = VertexAIEmbeddings(
            model_name=settings.EMBEDDING_MODEL, # text-embedding-004
            project=settings.PROJECT_ID,
            location=settings.LOCATION
        )
        self.vector_store = None

    def process_pdf(self, pdf_path):
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            
            if not text.strip():
                return "Error: El PDF no contiene texto extraíble."

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=settings.CHUNK_SIZE, 
                chunk_overlap=settings.CHUNK_OVERLAP
            )
            chunks = splitter.split_text(text)
            
            # Generar el índice FAISS
            self.vector_store = FAISS.from_texts(chunks, self.embeddings)
            return f"Procesados {len(chunks)} fragmentos con éxito."
        except Exception as e:
            return f"Error procesando PDF: {str(e)}"

    def get_answer(self, question):
        if not self.vector_store:
            return "Error: No hay documento cargado."
        
        docs = self.vector_store.similarity_search(question, k=4)
        context = "\n\n".join([d.page_content for d in docs])
        
        # Prompt optimizado para bilingüismo
        prompt = f"""Actúa como un asistente bilingüe (English, Spanish) experto. 
        Responde la pregunta del usuario utilizando únicamente el contexto proporcionado.
        Si el contexto está en un idioma diferente a la pregunta, traduce la información necesaria para responder con precisión.

        Contexto:
        {context}

        Pregunta del usuario: 
        {question}
        """
        return self.llm.invoke(prompt)