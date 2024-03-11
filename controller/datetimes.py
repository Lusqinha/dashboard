from datetime import datetime

INFO_MESES = {
                'Janeiro':{"nome": "Janeiro","dias": 31,"abrv": "Jan", "cod":'01'},
                'Fevereiro':{"nome": "Fevereiro","dias": 28,"abrv": "Fev", "cod":'02'},
                'Março':{"nome": "Março","dias": 31,"abrv": "Mar", "cod":'03'},
                'Abril':{"nome": "Abril","dias": 30,"abrv": "Abr", "cod":'04'},
                'Maio':{"nome": "Maio","dias": 31,"abrv": "Mai", "cod":'05'},
                'Junho':{"nome": "Junho","dias": 30,"abrv": "Jun", "cod":'06'},
                'Julho':{"nome": "Julho","dias": 31,"abrv": "Jul", "cod":'07'},
                'Agosto':{"nome": "Agosto","dias": 31,"abrv": "Ago", "cod":'08'},
                'Setembro':{"nome": "Setembro","dias": 30,"abrv": "Set", "cod":'09'},
                'Outubro':{"nome": "Outubro","dias": 31,"abrv": "Out", "cod":'10'},
                'Novembro':{"nome": "Novembro","dias": 30,"abrv": "Nov", "cod":'11'},
                'Dezembro':{"nome": "Dezembro","dias": 31,"abrv": "Dez", "cod":'12'},
            }

ANOS = range(2023, 2025)

LISTA_MESES = list(INFO_MESES.keys())


def data_atual() -> tuple[int, int, int]:
    """
    Retorna a data atual no formato (dia, mês, ano).

    Returns:
        tuple[int, int, int]: A data atual no formato (dia, mês, ano).
    """
    hoje_dia, hoje_mes, hoje_ano = datetime.now().day, datetime.now().month, datetime.now().year
    return hoje_dia, hoje_mes, hoje_ano
    