from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from infra.repository.treinos_repository import TreinosRepository
from infra.repository.exercicios_repository import ExercicioRepository
from pathlib import Path
from infra.entities.treinos import Treinos
from infra.entities.exercicio import Exercicio
from pydantic import BaseModel

class Treinos(BaseModel):
  nome: str|None = None
  id: int|None = None
  
class Exercicio(BaseModel):
  id : int|None = None
  nome : str|None = None
  repeticoes : str|None = None
  link : str|None = None
  treino_id : int|None = None


templates = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory="templates")
app = FastAPI(title="Arielton Palmeirense")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
  
@app.get("/treinos")
async def busca_treinos():
  repo = TreinosRepository()
  data = repo.select()
  return data 

@app.post("/treinos")
async def insere_treino(treino: Treinos):
  repo = TreinosRepository()
  repo.insert(treino)
  return {"message":"Treino criado com sucesso"}


@app.put("/treinos/{id}")
async def atualiza_treino(treino: Treinos,id:int):
  repo = TreinosRepository()
  repo.update(id,treino.nome)
  treino.id = id
  return treino

@app.delete("/treinos/{id}")
async def deleta_treino(id:int):
  repo = TreinosRepository()
  repo.delete(id)
  return {"message":"Treino deletado com sucesso"}


@app.get("/exercicios")
async def busca_exercicos():
  repo = ExercicioRepository()
  data = repo.select() 
  return data


@app.post("/exercicios")
async def insere_exercicio(exercicio: Exercicio):
  repo = TreinosRepository()
  repo.insert(exercicio)
  exercicio.id = id
  return {"message":"Exercício criado com sucesso"}


@app.put("/exercicios/{id}")
async def atualiza_exercicio(exercicio: Exercicio,id:int):
  repo = ExercicioRepository()
  repo.update(id,exercicio.nome,exercicio.repeticoes,exercicio.link,exercicio.treino_id)
  exercicio.id = id
  return exercicio

@app.delete("/exercicios/{id}")
async def deleta_exercicio(id:int):
  repo = TreinosRepository()
  repo.delete(id)
  return {"message":"Exercício deletado com sucesso"}
