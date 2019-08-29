import time
import os

def limpar_log(nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as f:
        pass

def encontrar_warnings(linha):
    data, level, arquivo, mensagem = linha.split('|')
    #print(data, level, arquivo, mensagem)
    if 'WARNING' in level and 'Falha na autenticação' in mensagem:
        #print(level)
        return True
    return False

def enviar_emails():
    pass

CONTADOR = 0

done = False
while not done:
    with open ('app.log', 'r') as f:
        for line in f.readlines():
            if encontrar_warnings(line.strip()):
                CONTADOR = CONTADOR + 1
            if CONTADOR == 3:
                enviar_emails()
                CONTADOR = 0
    limpar_log('app.log')
    time.sleep(1.0)
