from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Exercicio(Base):
    __tablename__ = "exercicio"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(36), nullable=False)
    repeticoes = Column(String(36), nullable=False)
    link = Column(String(36), nullable=False)
    treino_id = Column(Integer, ForeignKey("treino.id"), nullable=False)
    
    treino = relationship("Treinos", backref="exercicios", lazy=True)
    
    def __repr__(self):
        return f'Exercicio(nome={self.nome}, treino_id={self.treino_id}, repeticoes={self.repeticoes}, link={self.link})'
