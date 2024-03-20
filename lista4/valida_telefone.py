import re

def valida_telefone(numero):
    regex = r'^\([1-9]{2}\) [2-9][0-9]{3,4}\-[0-9]{4}$'
    return re.match(regex, numero) is not None
