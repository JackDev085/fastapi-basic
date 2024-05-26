import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).resolve().parent
conn = sqlite3.connect(ROOT_PATH/"teste.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS treino (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(100) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS exercicio (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  treino_id INT NOT NULL,
  nome VARCHAR(100) NOT NULL,
  repeticoes VARCHAR(50) NOT NULL,
  link VARCHAR(50) NOT NULL,
  FOREIGN KEY(treino_id) REFERENCES treino(id)
);
""")

