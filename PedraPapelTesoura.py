import random 


usuario = input("Escolha 'PD' para pedra, 'PA' para papel e 'TS' para tesoura: ")

comp = random.choice(['PD','PA','TS'])

if usuario == comp :
    print('Empate')

elif (usuario == 'PD' and comp == 'TS') or (usuario == 'TS' and comp == 'PA') or (usuario == 'PA' and comp == 'PD'): 
    print('Você venceu')

else:
    print('Você perdeu')



