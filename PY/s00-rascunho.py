import pandas as pd
from PY/teste.py import *


'Com base no Layout US do Teclado Simplificado Dvorak'
qwert = [' ', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç', '~', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', ';']
dvorak = [' ', "'", ',', '.', 'p', 'y', 'f', 'g', 'c', 'r', 'l', 'a', 'o', 'e', 'u', 'i', 'd', 'h', 't', 'n', 's', '_', ';', 'q', 'j', 'k', 'x', 'b', 'm', 'w', 'v', 'z']
len(qwert)
len(dvorak)

df = pd.DataFrame({'qwert':qwert, 'dvorak':dvorak})
df

def dvorak_encrypt(text):
    result = ""
    for i in range(len(text)):
        char = text[i].lower()
        result += df.dvorak[list(df.qwert).index(char)]
    return result

text = "qwert agora ja da de falar melhor"

print(f'Plain Text : {text}')
print(f'Cipher: {dvorak_encrypt(text)}')

