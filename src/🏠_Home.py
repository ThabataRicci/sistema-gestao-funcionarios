import streamlit as st
from database.models import init_db
from Footer import footer

st.set_page_config(page_title="Sistema de Análise", layout="wide")

init_db()

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.title("📊 Controle de Base de Dados")
    st.markdown("""
    Use o menu lateral para acessar as funcionalidades:
    
    - **Upload:** Envie arquivos CSV.
    - **Visualização:** Veja os dados carregados.
    - **Edição:** Edite os registros.
    - **Log de Operações:** Consulte o histórico de alterações.
    """)

footer()