import streamlit as st
from auth.login import set_authenticator, read_yaml

def main():
    """
    Função principal que realiza a autenticação do usuário.

    Retorna o nome de usuário se a autenticação for bem-sucedida.
    Caso contrário, exibe uma mensagem de erro.

    :return: O nome de usuário ou None
    """
    file = read_yaml("auth/auth.yaml")
    auth = set_authenticator(file)
    
    name, auth_status, username = auth.login()

    if auth_status:
        return username
    elif auth_status == False:
        st.error("Usuário ou senha incorretos!")
        
    return
        
        
    

