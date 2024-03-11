import numpy as np

def capacidade_produtiva(agr_disponivel:int, capacidade_atendimento_diario:int, atendimentos_realizados:int, data:str, ticket_medio:float):
    """
    Calcula a capacidade produtiva com base nos parâmetros fornecidos.

    Args:
        agr_disponivel (int): A quantidade de recursos disponíveis para atendimento.
        capacidade_atendimento_diario (int): A capacidade máxima de atendimento por dia.
        atendimentos_realizados (int): O número de atendimentos já realizados.
        data (str): A data em que o cálculo está sendo realizado.
        ticket_medio (float): O valor médio de cada atendimento.

    Returns:
        dict: Um dicionário contendo os resultados do cálculo, incluindo a capacidade ociosa,
        a porcentagem de ocupação, a porcentagem ociosa, o valor total perdido, e os parâmetros
        de entrada.

    """
    capacidade_ociosa = capacidade_atendimento_diario - atendimentos_realizados
    
    porcentagem_ocupacao = (atendimentos_realizados / capacidade_atendimento_diario) * 100
    porcentagem_ocioso = (capacidade_ociosa / capacidade_atendimento_diario) * 100
    
    total_perdido = capacidade_ociosa * ticket_medio
    
    output = {
        "data": data,
        "capacidade_ociosa": capacidade_ociosa,
        "porcentagem_ocupacao": porcentagem_ocupacao,
        "porcentagem_ocioso": porcentagem_ocioso,
        "total_perdido": total_perdido,
        "agr_disponivel": agr_disponivel,
        "capacidade_atendimento_diario": capacidade_atendimento_diario,
        "atendimentos_realizados": atendimentos_realizados,
        "ticket_medio": ticket_medio
    }
    
    return output

def total_colunas_vendas(df, colunas: list) -> dict:
    totais = {}
    
    for coluna in colunas:
        key = f"{coluna}"
        totais[key] = df[coluna].sum()
        
    return totais

def comparativo_parcial(total_mes_anterior, total_mes_atual, total_ano_anterior):
    parcial_mes = total_mes_atual/total_mes_anterior - 1
    parcial_ano = total_mes_atual/total_ano_anterior - 1
    
    return parcial_mes, parcial_ano

def comparativo_meta(meta:int, total_mes_atual):
    return meta, total_mes_atual

def linha_tendencia_exponencial(totais:tuple[int]):
    x = np.arange(1, len(totais)+1)
    y = np.array(totais)
    
    a, b = np.polyfit(x, np.log(y), 1)
    
    return np.exp(a*x + b)
