# db_connector.py
import sqlite3

def conectar(banco='data/exemplo.db'):
    conn = sqlite3.connect(banco)
    return conn
