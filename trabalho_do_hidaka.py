import random
import datetime

def cadastro_jogador():
    nick = input('Insira seu nickname: ')
    if nick[0] != '@':
        print('Nickname inválido. Deve iniciar com @')
        return
    
    return nick

def fase_adivinha():
    resposta = input('Adivinhe o numero: ')
    reposta = int(resposta)
    return reposta

def primeira_fase():
    numero = random.randint()
    numero = abs(numero)
    erros = 0

    reposta_usuario = fase_adivinha()

    while reposta_usuario != numero:
        print(erros, 'erros\n\n')
        if reposta_usuario > numero:
            print('Tente um numero menor.\n\n')
            reposta_usuario = fase_adivinha()
            erros += 1

        else:
            print('Tente um numero maior.\n\n')
            reposta_usuario = fase_adivinha()
            erros += 1

    return erros

def segunda_fase()


