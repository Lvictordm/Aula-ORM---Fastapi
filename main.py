from fastapi import FastAPI


# Inicializar o app fastapi
app = FastAPI(title="Gestão Escolar")

# Metodos http: GET - POST - PUT - DELETE
@app.get("/")
def tela_inicial():
    return {"Mensagem": "sistema de Gestão Escolar"}


# Banco de dados
usuario = {
    1: {"nome": "gabriel", "idade": 33 },
    1: {"nome": "zamboni", "idade": 17 },
    1: {"nome": "tomé", "idade": 18 },
}

@app.get("/alunos")
def listar_alunos():
    return {"usuarios": "usuarios"}