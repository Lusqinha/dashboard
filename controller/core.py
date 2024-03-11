from controller.datetimes import INFO_MESES, LISTA_MESES
from os import remove, makedirs
import pandas as pd


df_folder = "./dataframe"


def create_df(ano: int, unidade: str):

    df = pd.DataFrame()

    for mes in INFO_MESES.keys():

        mes_abrv = INFO_MESES[mes]["abrv"]
        ano_abrv = str(ano)[2:]
        df[f'{mes_abrv} {ano_abrv}'] = [None for _ in range(23)]

    # index starts at 1
    df.index += 1
    try:
        df.to_csv(f"{df_folder}/{unidade}/{ano}.csv",
                  index=True, index_label="Dia")
    except OSError:
        makedirs(f'{df_folder}/{unidade}')
        
    print(df.tail())
    return df


def create_geral_info_df(ano: int, mes: str, unidade: str):
    data_json = {
        "ticket_medio": 0,
        "meta_emissoes": 0,
        'meta_vendas': 0,
    }
    df = pd.DataFrame(data_json)
    try:
        df.to_csv(f"{df_folder}/{unidade}/{ano}_{mes}.csv",
                  index=False)
    except OSError:
        makedirs(f'{df_folder}/{unidade}')

    return df


def read_df(ano: int, unidade: str):
    try:
        df = pd.read_csv(f"{df_folder}/{unidade}/{ano}.csv")
        return df

    except FileNotFoundError:
        return None


def read_month_df(mes: str, ano: int, unidade: str):
    ano_abrv = str(ano)[2:]
    mes_abrv = INFO_MESES[mes]['abrv']

    try:

        df = pd.read_csv(f"{df_folder}/{unidade}/{ano}.csv")
        col = df[f'{mes_abrv} {ano_abrv}']

        return col

    except FileNotFoundError:
        return None


def save_update_df(df, ano: int, unidade: str):
    df.to_csv(f"{df_folder}/{unidade}/{ano}.csv", index=False)


def save_update_cols(df, ano: int, ano_anterior: int, unidade: str):
    """
    Saves and updates columns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing the columns to be saved and updated.
        ano (int): The current year.
        ano_anterior (int): The previous year.
        unidade (str): The unit associated with the DataFrame.

    Raises:
        FileNotFoundError: If the file is not found.

    Returns:
        None
    """

    try:
        year_df = read_df(ano, unidade)
        prev_year_df = read_df(ano_anterior, unidade)

    except FileNotFoundError:
        print("File not found")

    if year_df is not None:

        for col in df.columns:

            if col == "Dia" or col == "index":
                continue

            col_year = col.split(" ")[1]

            if ano_anterior == 2000+int(col_year) and prev_year_df is not None:
                try:
                    prev_year_df[col] = df[col]
                    continue
                except:
                    print("Error")
                    continue

            year_df[col] = df[col]
    elif year_df is None:
        raise FileNotFoundError("File not found")

    try:
        year_df.to_csv(f"{df_folder}/{unidade}/{ano}.csv", index=False)
        prev_year_df.to_csv(f"{df_folder}/{unidade}/{ano_anterior}.csv", index=False)  # type: ignore
    except OSError:
        makedirs(f"{df_folder}/{unidade}")


def merge_df(df1, df2):
    return pd.merge(df1, df2, on="Dia")


def format_df(ano: int, mes: str, unidade: str):
    """
    Função responsável por selecionar as colunas do DataFrame principal.

    Args:
        ano (int): O ano a ser exibido.
        mes (str): O mês a ser exibido.
        mes_anterior (str): O mês anterior ao mês a ser exibido.
        unidade (str): A unidade a ser exibida.

    Returns:
        pd.DataFrame: O DataFrame formatado.
    """

    ano_anterior = ano-1
    mes_anterior = LISTA_MESES[LISTA_MESES.index(mes)-1]

    col_dia = [i for i in range(1, 24)]
    col_dia = pd.DataFrame(col_dia, columns=["Dia"])

    col_mes_atual = read_month_df(mes, ano, unidade)
    col_mes_anterior = read_month_df(mes_anterior, ano, unidade)
    col_ano_anterior = read_month_df(mes, ano_anterior, unidade)

    output_df = pd.DataFrame()

    output_df["Dia"] = col_dia['Dia']
    output_df[f"{INFO_MESES[mes_anterior]['abrv']} {str(ano)[2:]}"] = col_mes_anterior
    output_df[f"{INFO_MESES[mes]['abrv']} {str(ano_anterior)[2:]}"] = col_ano_anterior
    output_df[f"{INFO_MESES[mes]['abrv']} {str(ano)[2:]}"] = col_mes_atual

    print(output_df.head())

    return output_df


def delete_df(unidade: str, ano: int):
    remove(f"{df_folder}/{unidade}/{ano}.csv")


if __name__ == "__main__":
    df = create_df(2022, 'Pelotas')
