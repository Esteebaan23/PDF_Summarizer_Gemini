from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_ID: str = "rag-summarize" # Confirmado por tu imagen
    LOCATION: str = "us-central1"
    # Cambiamos a la versión específica estable
    MODEL_NAME: str = "gemini-2.5-flash" 
    EMBEDDING_MODEL: str = "text-multilingual-embedding-002"
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 100
    PORT: int = 8080

    class Config:
        env_file = ".env"

settings = Settings()