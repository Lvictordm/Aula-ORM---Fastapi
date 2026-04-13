from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Aluno, Curso

#import a biblioteca:
#pip install jinja2 python-multipart

# python -m uvicorn main:app --reload

# Inicializar o app fastapi
app = FastAPI(title="Gestão Escolar")

# Aponta para pasta onde fica os hmtl
templates = Jinja2Templates(directory="templates")

# Metodos http: GET - POST - PUT - DELETE

# ROtas inicial

# Para exibir um html na rota - Exibe o formulario
@app.get("/cursos/cadastro", response_class=HTMLResponse)
def exibir_cadastro(request: Request):
    return templates.TemplateResponse(request, "cadastro_curso.html", {"request": request})
