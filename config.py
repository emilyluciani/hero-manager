# config.py
import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",  # coloque sua senha se tiver
    "database": "heromanager"
}

SECRET_KEY = "chave-super-secreta-aqui"   # pode trocar depois

def get_db():
    """
    Retorna uma conexão ativa com o banco MySQL utilizando o DB_CONFIG.
    """
    return mysql.connector.connect(**DB_CONFIG)