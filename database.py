from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
import warnings

# Carregar as variáveis do arquivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    warnings.warn(
        "DATABASE_URL não definida. Usando fallback sqlite:///./dev.db. Defina DATABASE_URL em um arquivo .env para produção.",
        UserWarning,
    )
    DATABASE_URL = "sqlite:///./dev.db"

# Para SQLite, precisamos desse argumento extra
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para todos os models do banco
Base = declarative_base()