import streamlit as st
import sqlite3
import pandas as pd
from database.models import init_db, registrar_log
from database.constants import MAPEAMENTO_LOG, aplicar_nomes_amigaveis
from Footer import footer

col1, col2, col3 = st.columns([1,2,1])

# Página de log
def page_log():
    with col2:
        st.title("🗂️ Log de Operações")
    
        conn = sqlite3.connect('dados.db')
        df = pd.read_sql("SELECT * FROM log_operacoes ORDER BY data_hora DESC", conn)
        df = aplicar_nomes_amigaveis(df, MAPEAMENTO_LOG)
        conn.close()
    
        st.dataframe(df)

page_log()
footer()