from infra.configs.connection import DBConnectionHandler
from infra.entities.exercicio import Exercicio


class ExercicioRepository:
  def select(self):
    with DBConnectionHandler() as db:
      data = db.session.query(Exercicio).all()
      return data
    
  def insert(self,treino_id,nome, repeticoes):
    with DBConnectionHandler() as db:
      try:
        data_insert = Exercicio(treino_id=treino_id ,nome=nome, repeticoes=repeticoes)
        db.session.add(data_insert)
        db.session.commit()
      except Exception:
        db.session.rollback()
        raise Exception 
      
  def delete(self, id):
    with DBConnectionHandler() as db:
      db.session.query(Exercicio).filter(Exercicio.id==id).delete()
      db.session.commit()
      
  def update(self, id,treino_id,nome, repeticoes):
    with DBConnectionHandler() as db:
      db.session.query(Exercicio).filter(Exercicio.id==id).update({"treino_id":treino_id, "nome":nome, "repeticoes":repeticoes})
      db.session.commit()