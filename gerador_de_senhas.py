import random


quanti = input('insira o numero de senhas desejadas: ')
size = input('insira o tamanho das senhas: ')

quanti = int(quanti)
size = int(size)


# 3 listas que possuem todos os caracteres possiveis das senhas

letra_M = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letra_m = 'abcdefghijklmnopqrstuvwxyz'
algarismos = '0123456789'


# as 3 funções seguintes que irão escolher os caracteres das suas respectivas listas

def funcao_m():
    letra_escolhida = random.choice(letra_m)
    return letra_escolhida

def funcao_M():
    LETRA_escolhida = random.choice(letra_M)
    return LETRA_escolhida 

def num():
    numero_escolhido = random.choice(algarismos)
    return numero_escolhido

lista_de_funcoes = [num, funcao_M, funcao_m]


# laço que fomará a quantidade de senhas especificadas pelo usuario
while quanti > 0:
    senha = ''

    # laço que construirá as senhas no tamanho certo
    for _ in range(size):
        caractere_escolhido = random.choice(lista_de_funcoes)()
        senha += caractere_escolhido
    
    quanti -= 1
    print(senha)