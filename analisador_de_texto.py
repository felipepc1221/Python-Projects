import math

texto_base = input('Insira o texto a ser analisado aqui: ')

def analise_texto(texto):
    """
    Função que recebe um texto e retorna o numero de caracteres, palavras e 
    o tempo estimado de leitura.

    Argumento: texto

    Retorno: numero de caracteres, numero de palavras e tempo de leitura estimado.
    """
    
    palavras = texto.split()

    palavras_filtradas = [word for word in palavras if not (word.isdigit() or word in ('<', '>', '=', '+', '%'))]   

    numero_palavras = len(palavras_filtradas)

    numero_caracteres = len(texto)

    tempo_leitura_final = math.ceil(numero_palavras / 150)

    return f'De acordo com o texto fornecido:\nNumero de palavras: {numero_palavras}\nNumero de caracteres: {numero_caracteres}\nTempo de leitura estimado: {tempo_leitura_final} minutos.'

print(analise_texto(texto_base))