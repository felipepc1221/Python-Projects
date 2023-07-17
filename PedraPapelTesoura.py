import random 


usuario = input("Escolha 'PD' para pedra, 'PA' para papel e 'TS' para tesoura: ")

#definindo a escolha da maquina
comp = random.choice(['PD','PA','TS'])

#modelo de decisão if/elif/else que determina vitoria,derrota ou empate
if usuario == comp :
    print('Empate')

elif (usuario == 'PD' and comp == 'TS') or (usuario == 'TS' and comp == 'PA') or (usuario == 'PA' and comp == 'PD'): 
    print('Você venceu')

else:
    print('Você perdeu')



