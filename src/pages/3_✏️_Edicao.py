import streamlit as st
import sqlite3
import pandas as pd
from database.models import init_db, registrar_log
from database.constants import MAPEAMENTO_FUNCIONARIOS, MAPEAMENTO_CONVENIO, aplicar_nomes_amigaveis
from Footer import footer

col1, col2, col3 = st.columns([1,2,1])

# Página de edição
def page_edit():
    with col2:
        st.title("✏️ Edição de Dados")
    
        tabela = st.selectbox("Selecione a tabela para editar:", 
                            ["Funcionários", "Uso de Convênio"])
    
        conn = sqlite3.connect('dados.db')
    
        if tabela == "Funcionários":
            df = pd.read_sql("SELECT * FROM funcionarios", conn)
            df_display = aplicar_nomes_amigaveis(df.copy(), MAPEAMENTO_FUNCIONARIOS)
            id_col = "id_funcionario"
            nome_id = "ID do Funcionário"
        else:
            df = pd.read_sql("SELECT * FROM uso_convenio", conn)
            df_display = aplicar_nomes_amigaveis(df.copy(), MAPEAMENTO_CONVENIO)
            id_col = "id_uso"
            nome_id = "ID do Uso"
    
        st.dataframe(df_display)
    
        st.subheader("Editar Registro")
        id_editar = st.number_input(f"{nome_id} do registro para editar:", min_value=1)
    
        if st.button("Carregar Registro"):
            registro = pd.read_sql(f"SELECT * FROM {tabela.lower().replace('ê', 'e')} WHERE {id_col} = {id_editar}", conn)
            if registro.empty:
                st.warning("Registro não encontrado!")
            else:
                st.session_state.registro_editar = registro.iloc[0].to_dict()
    
        if 'registro_editar' in st.session_state:
            registro = st.session_state.registro_editar
        
            if tabela == "Funcionários":
                novo_nome = st.text_input("Nome Completo:", value=registro['nome'])
                novo_cpf = st.text_input("CPF:", value=registro['cpf'])
                novo_data_nasc = st.text_input("Data de Nascimento:", value=registro['data_nascimento'])
                novo_empresa = st.text_input("Empresa:", value=registro['empresa'])
                novo_cnpj = st.text_input("CNPJ:", value=registro['cnpj'])
            
                if st.button("Salvar Alterações"):
                    c = conn.cursor()
                    c.execute(f"""UPDATE funcionarios SET 
                            nome = ?, cpf = ?, data_nascimento = ?, empresa = ?, cnpj = ?
                            WHERE id_funcionario = ?""",
                            (novo_nome, novo_cpf, novo_data_nasc, novo_empresa, novo_cnpj, id_editar))
                    conn.commit()
                    registrar_log("EDIÇÃO", "funcionarios")
                    st.success("Registro atualizado com sucesso!")
                    del st.session_state.registro_editar
            else:
                novo_nome_convenio = st.text_input("Nome do Convênio:", value=registro['nome_convenio'])
                novo_tipo_convenio = st.text_input("Tipo do Convênio:", value=registro['tipo_convenio'])
                novo_data_uso = st.text_input("Data de Uso:", value=registro['data_uso'])
                novo_tipo_atendimento = st.text_input("Tipo de Atendimento:", value=registro['tipo_atendimento'])
                novo_id_funcionario = st.number_input("ID do Funcionário:", value=registro['id_funcionario'])
            
                if st.button("Salvar Alterações"):
                    c = conn.cursor()
                    c.execute(f"""UPDATE uso_convenio SET 
                            nome_convenio = ?, tipo_convenio = ?, data_uso = ?, 
                            tipo_atendimento = ?, id_funcionario = ?
                            WHERE id_uso = ?""",
                            (novo_nome_convenio, novo_tipo_convenio, novo_data_uso, 
                            novo_tipo_atendimento, novo_id_funcionario, id_editar))
                    conn.commit()
                    registrar_log("EDIÇÃO", "uso_convenio")
                    st.success("Registro atualizado com sucesso!")
                    del st.session_state.registro_editar
    
        conn.close()

page_edit()
footer()