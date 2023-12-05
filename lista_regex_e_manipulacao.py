import re
import csv

def open_file(file_path):
    with open(file_path, 'r', encoding = "utf-8", newline = '') as f:
        leitor_csv = csv.reader(f)
        lista_maior = list(leitor_csv)
    return lista_maior

#datatran2020.csv, 12 colunna fase_dia é 11
def distintos_fase_dia(caminho_arquivo):
    lista_fase_dia = []

    #abre o arquivo e separa as linhas da tabela em listas dentro da lista_maior
    lista_maior = open_file(caminho_arquivo)
    for i in range(len(lista_maior)):
        fase_dia = lista_maior[i]
        lista_fase_dia.append(fase_dia[11])

    lista_sem_repet = list(set(lista_fase_dia))
    resultado = len(lista_sem_repet)
    res = 'valores distintos na coluna fase_dia: '


    return resultado


def obitos_PA(caminho_arquivo):
    contador = 0
    #coluna 4 é uf, 18 é mortos

    lista_maior = open_file(caminho_arquivo)
    for i in lista_maior:
        if i[4] == 'PA':
            num_obitos = int(i[18])
            contador += num_obitos

    return contador

def uf_mais_obitos(caminho_arquivo):
    lista_maior = open_file(caminho_arquivo)
    lista_de_uf = []
    for i in lista_maior:
        if i[4] not in lista_de_uf:
            lista_de_uf.append(i[4])

    lista_de_uf.pop(0)

    
    lista_de_lista_de_uf_vazio = []
    for i in lista_de_uf:
        uf = []
        lista_de_lista_de_uf_vazio.append(uf)


    for i in lista_maior:
        if i[14] == 'Dupla':
            mortos = i[18]
            uf = i[4]
            indice = lista_de_uf.index(uf)
            
            lista_de_lista_de_uf_vazio[indice].append(mortos)
    
    lista_soma = []

    for lista in lista_de_lista_de_uf_vazio:
        nova_lista = [int(elemento) for elemento in lista]
        soma = sum(nova_lista)
        lista_soma.append(soma)

    lista_soma_copia = lista_soma
    lista_indice_maiores = []

    for i in range(3):
        maximo = max(lista_soma)
        indice = lista_soma_copia.index(maximo)
        lista_indice_maiores.append(indice)
        lista_soma.remove(maximo)

    primeiro_lugar_indice = lista_indice_maiores[0]
    primeiro_lugar_uf = lista_de_uf[primeiro_lugar_indice]

    segundo_lugar_indice = lista_indice_maiores[1]
    segundo_lugar_uf = lista_de_uf[segundo_lugar_indice]

    terceiro_lugar_indice = lista_indice_maiores[2]
    terceiro_lugar_uf = lista_de_uf[terceiro_lugar_indice]

    return primeiro_lugar_uf, segundo_lugar_uf, terceiro_lugar_uf

print(uf_mais_obitos("datatran2020.csv"))



    

    






