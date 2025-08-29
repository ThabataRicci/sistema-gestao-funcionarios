import streamlit as st
import sqlite3
import pandas as pd
from database.models import init_db, registrar_log
from Footer import footer

col1, col2, col3 = st.columns([1,2,1])

# Página de upload
def page_upload():
    with col2:
        st.title("Upload de Arquivos CSV")
    
        st.subheader("Funcionários")
        file_funcionarios = st.file_uploader("Selecione o arquivo CSV de funcionários", type=['csv'], key='funcionarios')
    
        st.subheader("Uso de Convênio")
        file_convenio = st.file_uploader("Selecione o arquivo CSV de uso de convênio", type=['csv'], key='convenio')
    
        if st.button("Carregar Dados"):
            if file_funcionarios is not None and file_convenio is not None:
                try:
                    df_funcionarios = pd.read_csv(file_funcionarios)
                    df_convenio = pd.read_csv(file_convenio)
                
                    conn = sqlite3.connect('dados.db')
                
                    df_funcionarios.to_sql('funcionarios', conn, if_exists='replace', index=False)
                    registrar_log("CARGA DE DADOS", "funcionarios")
                
                    df_convenio.to_sql('uso_convenio', conn, if_exists='replace', index=False)
                    registrar_log("CARGA DE DADOS", "uso_convenio")
                
                    conn.close()
                    st.success("Dados carregados com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao carregar dados: {e}")
            else:
                st.warning("Por favor, faça upload de ambos os arquivos.")

page_upload()
footer()