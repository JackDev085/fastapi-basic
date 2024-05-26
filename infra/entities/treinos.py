from infra.configs.base import Base
from sqlalchemy import Column, Integer, String


class Treinos(Base):
    __tablename__ = "treino"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)

    def __repr__(self):
        return f'Treino(nome={self.nome})'
