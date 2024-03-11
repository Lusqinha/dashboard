import plotly.graph_objects as go

def velocimentro(valor_atual, valor_anterior, meta):
    
    if valor_anterior == 0 and valor_atual != 0:
        valor_anterior = 0
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        delta={'reference': valor_anterior, 
               'increasing': {'color': "#8cdb7b"}, 
               'decreasing': {'color': "red"}},
        value = valor_atual,
        title = {'text': "Vendas/Ticket"},
        gauge = {
            'axis': {'range': [None, meta]},
            'bar': {'color': "#1B262C", 'thickness': 0},
            'steps' : [
                {'range': [0, meta//5], 'color': "#ff4136"},
                {'range': [meta//5, meta//2], 'color': "#EEF296"},
                {'range': [meta//2, meta//1.25], 'color': "#9ADE7B"},
                {'range': [meta//1.25, meta], 'color': "#3d9970"}
            ], 'threshold': {'line': {'color': "#990000", 'width': 3}, 'thickness': 0.80, 'value': valor_atual}
        }
    ))
    return fig

def grafico_linha(df, title:str, total_atual:int, total_anterior:int, meta:int|None=None):
    fig = go.Figure(go.Indicator(
        mode='number+delta',
        value=total_atual,
        delta={
            'reference': total_anterior,
            'valueformat': '.0f'
        },
        title={'text': "Vendas do mês"},
        domain={'x': [0, 1], 'y': [0, 1]} 
    ))  
    for col in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[col], mode='lines', name=col))
    
    
    
    return fig

def parcial_display(total_ant, total_at, total_ano_ant, mes_ano_ant:str, mes_ano_at:str, ano_ant:str):
    """
    Cria um gráfico de indicadores com o comparativo parcial entre dois períodos.

    Args:
        total_ant (float): Total do período anterior.
        total_at (float): Total do período atual.
        total_ano_ant (float): Total do ano anterior.
        mes_ano_ant (str): Mês e ano do período anterior.
        mes_ano_at (str): Mês e ano do período atual.
        ano_ant (str): Ano do período anterior.

    Returns:
        go.Figure: Gráfico de indicadores com o comparativo parcial.
    """
    
    fig = go.Figure()
    
    if total_ant == 0 and total_at != 0:
        total_ant = 1
        
    if total_ano_ant == 0 and total_at != 0:
        total_ano_ant = 1
    
    fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = total_at,
    title = {"text": f"<span>Comparativo Parcial</span><br><span style='font-size:0.8em;color:gray'>{mes_ano_ant} x {mes_ano_at}</span><br><span style='font-size:0.8em;color:gray'>{mes_ano_ant}: {total_ant}</span>"},
    delta = {'reference': total_ant, 'relative': True},
    domain = {'x': [0, 1], 'y': [0.5, 1]},
    ))
    
    fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = total_at,
    title = {"text": f"<span>Comparativo Parcial</span><br><span style='font-size:0.8em;color:gray'>{ano_ant} x {mes_ano_at}</span>"},
    delta = {'reference': total_ano_ant, 'relative': True},
    domain = {'x': [0, 1], 'y': [0, 0.3]}))
    
    # round delta values to 2 decimal places
    fig.update_traces(delta_valueformat = '.1%')
    
    return fig