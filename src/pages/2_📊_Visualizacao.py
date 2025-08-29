import streamlit as st
import sqlite3
import pandas as pd
from database.models import init_db
from database.constants import MAPEAMENTO_FUNCIONARIOS, MAPEAMENTO_CONVENIO, MAPEAMENTO_LOG, aplicar_nomes_amigaveis
from Footer import footer

col1, col2, col3 = st.columns([1,2,1])

# Página de visualização
def page_view():
    with col2:
        st.title("📊 Visualização de Dados")
    
        tabela = st.selectbox("Selecione a tabela para visualizar:", 
                         ["Funcionários", "Uso de Convênio", "Log de Operações"])
    
        conn = sqlite3.connect('dados.db')
    
        if tabela == "Funcionários":
            df = pd.read_sql("SELECT * FROM funcionarios", conn)
            df = aplicar_nomes_amigaveis(df, MAPEAMENTO_FUNCIONARIOS)
        elif tabela == "Uso de Convênio":
            df = pd.read_sql("SELECT * FROM uso_convenio", conn)
            df = aplicar_nomes_amigaveis(df, MAPEAMENTO_CONVENIO)
        else:
            df = pd.read_sql("SELECT * FROM log_operacoes ORDER BY data_hora DESC", conn)
            df = aplicar_nomes_amigaveis(df, MAPEAMENTO_LOG)
    
        conn.close()
        st.dataframe(df)

page_view()
footer()