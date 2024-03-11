
from graph.analyser import total_colunas_vendas, linha_tendencia_exponencial
from graph.plot import velocimentro, grafico_linha, parcial_display
from controller.datetimes import data_atual
from controller.core import format_df
import streamlit as st

dia_atual, mes_atual, ano_atual = data_atual()

def screen(mes:str, ano:int, unidade:str):
    """
    Função responsável por exibir a tela do dashboard.

    Args:
        mes (str): O mês desejado.
        ano (int): O ano desejado.
        unidade (str): A unidade desejada.

    Returns:
        None
    """
    df = format_df(ano, mes, unidade)
    colunas = list(df.columns)
    colunas.pop(0)
    
    combined_df = df.copy()

    combined_df.set_index('Dia', inplace=True)

    totais = total_colunas_vendas(df, colunas)
    
    st.plotly_chart(grafico_linha(combined_df, f"Vendas {mes}/{ano}",int(totais[colunas[0]]), int(totais[colunas[2]]) ), use_container_width=True)
        
    left_col, right_col = st.columns(2)
    
    with left_col:
        with st.container(border=True):  
            parcial = parcial_display(
                ano_ant=f"{ colunas[1] }",
                total_ant=int(totais[colunas[0]]),
                total_at=int(totais[colunas[2]]),
                mes_ano_ant=f"{colunas[0]}",
                mes_ano_at=f"{colunas[2]}",
                total_ano_ant=int(totais[colunas[1]]),
            )  
            st.plotly_chart(parcial, use_container_width=True)  
            
    with right_col:
        
        with st.container(border=True):
            velocimentro_plot = velocimentro(int(totais[colunas[0]]), int(totais[colunas[2]]), 1000)
            st.plotly_chart(velocimentro_plot, use_container_width=True)
            
