from controller.core import create_df, read_df, save_update_cols, format_df
from controller.datetimes import INFO_MESES
import streamlit as st


def screen(mes: str | None, ano: int | None, unidade:str):
    """
    Função responsável por exibir a tela de acompanhamento mensal.

    Args:
        mes (str|None): O mês a ser exibido. Pode ser None caso não seja informado.
        ano (int|None): O ano a ser exibido. Pode ser None caso não seja informado.
        unidade (str): A unidade a ser exibida.

    Returns:
        None
    """
    if mes is None or ano is None:
        return

    if read_df(ano, unidade) is None:
        create_df(ano, unidade)

    
    with st.container(border=True):
        col_1, col_2 = st.columns(2)
        with col_1:
            file_csv = st.file_uploader("Upload de arquivo", type="csv", accept_multiple_files=False)
        with col_2:
            
            dia = st.number_input("Dia", min_value=1, max_value=23)
            
            if st.button("Enviar arquivo"): 
                if file_csv is not None:
                    st.success("Atualizado com sucesso.")
                else:
                    st.error("Erro ao atualizar. Nenhum arquivo foi selecionado.")
    

    df = format_df(ano, mes, unidade)

    with st.expander("Tabela para edição"):
        edited_df = st.data_editor(
            df, width=1000, height=800, hide_index=True, disabled=('Dia'))  # type: ignore

        if st.button("Salvar"):
            try:
                edited_df = edited_df.reset_index()
                save_update_cols(edited_df, ano, ano-1, unidade)
                st.success("Salvo com sucesso.")
            except Exception as e:
                st.error("Erro ao salvar. Erro: " + str(e))
                raise e
