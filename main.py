from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Curso, Aluno

# Import a biblioteca:
# pip install jinja2 python-multipart

# inicializar o app fastapi
app = FastAPI(title="Gestão escolar")

#Aponta para pasta onde ficam os html
templates = Jinja2Templates(directory="templates")

# Metodos http: GET, POST, PUT, DELETE

#Para exibir um html na rota - exibir o formulário
@app.get("/cursos/cadastro", response_class=HTMLResponse)
def exibir_cadastro(request: Request):
    return templates.TemplateResponse(request, "cadastro_curso.html", {"request": request})
