# Dicionários de mapeamento para nomes amigáveis
MAPEAMENTO_FUNCIONARIOS = {
    'id_funcionario': 'ID do Funcionário',
    'nome': 'Nome Completo',
    'cpf': 'CPF',
    'data_nascimento': 'Data de Nascimento',
    'empresa': 'Empresa',
    'cnpj': 'CNPJ'
}

MAPEAMENTO_CONVENIO = {
    'id_uso': 'ID do Uso',
    'nome_convenio': 'Nome do Convênio',
    'tipo_convenio': 'Tipo do Convênio',
    'data_uso': 'Data de Uso',
    'tipo_atendimento': 'Tipo de Atendimento',
    'id_funcionario': 'ID do Funcionário'
}

MAPEAMENTO_LOG = {
    'id_log': 'ID do Log',
    'operacao': 'Operação Realizada',
    'tabela': 'Tabela Afetada',
    'data_hora': 'Data e Hora'
}

# Função para aplicar os nomes amigáveis
def aplicar_nomes_amigaveis(df, mapeamento):
    return df.rename(columns=mapeamento)