from infra.configs.connection import DBConnectionHandler
from infra.entities.treinos import Treinos

class TreinosRepository:
  def select(self):
    with DBConnectionHandler() as db:
      data = db.session.query(Treinos).all()
      return data
    
  def insert(self, treino):
    data = (treino.nome,)
    with DBConnectionHandler() as db:
      try:
        data_insert = Treinos(nome=data[0])
        db.session.add(data_insert)
        db.session.commit()
      except Exception:
        db.session.rollback()
        raise Exception 
      
  def delete(self, id):
    with DBConnectionHandler() as db:
      db.session.query(Treinos).filter(Treinos.id==id).delete()
      db.session.commit()
      
  def update(self, id,nome):
    with DBConnectionHandler() as db:
      db.session.query(Treinos).filter(Treinos.id==id).update({"nome":nome})
      db.session.commit()