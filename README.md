# 🤖 Multilingual RAG System – Google Vertex AI

A **cloud-native Retrieval-Augmented Generation (RAG) application** for multilingual document summarization and question answering.  
This system integrates **Google Gemini (Vertex AI)**, **LangChain**, and **FAISS** to provide fast, accurate, and scalable document intelligence from PDF files.

The application is fully containerized and designed for production-ready deployment.

---

## 🚀 Key Features

- **Multilingual Document Intelligence**  
  Supports cross-lingual retrieval and generation, allowing users to query documents in a different language from the original content.

- **Google Vertex AI Integration**  
  Uses Gemini models and multilingual embeddings hosted on Vertex AI for low-latency, high-quality inference.

- **End-to-End RAG Orchestration**  
  Combines document ingestion, semantic retrieval, and answer generation using LangChain.

- **Scalable Backend**  
  Built with FastAPI to handle asynchronous requests efficiently.

- **Modern Conversational Interface**  
  Provides an interactive chat-based UI using Gradio, integrated directly with the backend.

- **Fully Containerized Deployment**  
  Easy setup and reproducible environments using Docker and Docker Compose.

---

## 🛠️ Tech Stack

- **LLM:** Google Gemini (Vertex AI)
- **Embeddings:** Multilingual embeddings (Vertex AI)
- **RAG Orchestration:** LangChain
- **Vector Store:** FAISS
- **Backend & API:** FastAPI (Python 3.10)
- **UI:** Gradio
- **Containerization:** Docker & Docker Compose
- **Cloud Platform:** Google Cloud Platform (Vertex AI)

---

## 📦 Installation & Setup

### 1️⃣ Prerequisites

Make sure you have the following installed and configured:

- A **Google Cloud Platform (GCP)** account
- **Vertex AI API enabled** in your GCP project
- **Docker** and **Docker Compose**


---

### 2️⃣ Run the Application

Clone the repository and start the application with:

```bash
docker-compose up --build
```

Once the containers are running, the application will be available at:
```
http://localhost:8080
```

📂 Project Structure

```
rag-google-app/
├── backend/                      # Core system logic
│   ├── __init__.py               # Marks the folder as a Python module
│   ├── main.py                   # Entry point: FastAPI + Gradio interface
│   ├── services.py               # RAG orchestration (LangChain, Vertex AI, FAISS)
│   └── schemas.py                # Data models (Pydantic) for request validation
│
├── config/                       # Environment configuration
│   ├── __init__.py
│   └── settings.py               # GCP variables (Project ID, models, region)
│
├── gcloud_config/                # Secure authentication directory
│   └── application_default_credentials.json
│                                  # Google Cloud access credentials
│
├── Dockerfile                    # Container image build instructions
├── docker-compose.yml            # Service orchestration and volume mounting
└── requirements.txt              # Python dependencies (FastAPI, LangChain, etc.)

```
