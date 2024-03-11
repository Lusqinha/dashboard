from controller.datetimes import INFO_MESES, ANOS, data_atual
from view import auth, registrar, dashboard
import streamlit as st

MESES = list(INFO_MESES.keys())

hoje_dia, hoje_mes, hoje_ano = data_atual()

UNIDADES = ["Unidade 1", "Unidade 2", "Unidade 3", "Unidade 4", "Unidade 5", "Unidade 6", "Unidade 7", "Unidade 8", "Unidade 9", "Unidade 10"]

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="centered")

def admin_page():
    with st.sidebar:
        st.title("Painel Diretor")
        st.divider()
        selected_unidade  = st.selectbox("Selecione a unidade", UNIDADES)
        selected_mes = st.selectbox("Selecione um mês", MESES, index=hoje_mes-1)
        selected_ano = st.selectbox("Selecione um ano", ANOS, index=ANOS.index(hoje_ano))
        st.divider()
        selected_window = st.radio("Selecione uma janela", ["Dashboard", "Configurações"])     

    match selected_window:
        case "Dashboard":
            dashboard.screen(selected_mes, selected_ano, selected_unidade)
        case "Configurações":
            dashboard.screen(selected_mes, selected_ano, selected_unidade)

def gestor_page():
    with st.sidebar:
        st.title("Painel Gestor")
        st.divider()
        selected_unidade  = st.selectbox("Selecione a unidade", UNIDADES)
        selected_mes = st.selectbox("Selecione um mês", MESES, index=hoje_mes-1)
        selected_ano = st.selectbox("Selecione um ano", ANOS, index=ANOS.index(hoje_ano))
        st.divider()
        selected_window = st.radio("Selecione uma janela", ["Dashboard", "Entrada de Dados"])     
        
    match selected_window:
        case "Entrada de Dados":
            registrar.screen(selected_mes, selected_ano, selected_unidade)
        case "Dashboard":
            dashboard.screen(selected_mes, selected_ano, selected_unidade)

def main():
    user = auth.main()
    
    match user:
        case "admin":
            admin_page()
        case "gestor":
            gestor_page()

if __name__ == "__main__":
    main()
