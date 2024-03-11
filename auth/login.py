from streamlit_authenticator import Authenticate
from yaml.loader import SafeLoader
import yaml


def read_yaml(file:str) -> dict:
    with open(file) as f:
        return yaml.load(f, Loader=SafeLoader)
  

def set_authenticator(file:dict) -> Authenticate:
    """
    Creates an instance of the Authenticate class based on the provided file dictionary.

    Args:
        file (dict): A dictionary containing the necessary information for authentication.

    Returns:
        Authenticate: An instance of the Authenticate class.

    """
    authenticator = Authenticate(
        file['credentials'],
        file['cookie']['name'],
        file['cookie']['key'],
        file['cookie']['expiry_days'],
        file['preauthorized']
    )  
    return authenticator
