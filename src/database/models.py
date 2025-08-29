import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS funcionarios
                 (id_funcionario INTEGER PRIMARY KEY,
                  nome TEXT,
                  cpf TEXT,
                  data_nascimento TEXT,
                  empresa TEXT,
                  cnpj TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS uso_convenio
                 (id_uso INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome_convenio TEXT,
                  tipo_convenio TEXT,
                  data_uso TEXT,
                  tipo_atendimento TEXT,
                  id_funcionario INTEGER)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS log_operacoes
                 (id_log INTEGER PRIMARY KEY AUTOINCREMENT,
                  operacao TEXT,
                  tabela TEXT,
                  data_hora TEXT)''')
    
    conn.commit()
    conn.close()

def registrar_log(operacao, tabela):
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO log_operacoes (operacao, tabela, data_hora) VALUES (?, ?, ?)",
              (operacao, tabela, data_hora))
    conn.commit()
    conn.close()