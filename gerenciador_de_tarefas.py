def primeiro_comando(comando=0):
    """
    função que define o comando a ser executador pelo gerenciador de tarefas

    argumentos:
    sempre 0, o argumento é atualizado para o valor de uso real dentro da propria função(input)

    retorno:
    numero que define qual será a ação do gerenciador 
    """

    print('Bem-vindo ao gerenciador de tarefas. Escolha a opção desejada digitando o numero correspondente:')
    print('1- Adicionar nova tarefa')
    print('2- Remover tarefa pendente')
    print('3- Visualizar todas as tarefas pendentes')
    print('4- Visualizar todas as tarefas concluídas')
    print('5- Concluir tarefa pendente')

    #variavel "comando" abriga a tarefa a ser executada
    comando = input('')                                                                    
    print('')
                                            
    comando = int(comando)
    return comando

        

#listas das tarefas no inicio do processo
tarefas_pendentes = []
tarefas_concluidas = []


def retorno_processo(a=0):
    """
    função retorno_processo pergunta ao usuario se o processo deve seguir 

    argumentos:
    sempre 0, o argumento é atualizado para o valor de uso real dentro da propria função(input)

    retorno:
    numero que define se o gerenciador deve ou não seguir funcionando
    """


    print('Deseja realizar uma nova ação?(digite o numero correspondente) ')
    print('1- Sim')
    print('2- Não')
    a = input('')
    a_int = int(a)


    # condicional que valida "a" e armazena o retorno da função
    if a_int == 1:
        print('')
        return True 
    
    elif a_int == 2:
        print('')
        return False
    
    else:
        print('Numeração inválida')
        print('')

#loop garante que o processo funcionará até que o usuário o interrompa
while True:

    comando = primeiro_comando()

    # condicionais que armazenam o codigo das ações do gerenciador

    #adiciona nova tarefa
    if comando == 1:
        nova_tarefa = input('Insira a nova tarefa: ')

        #adiciona a nova tarefa na lista
        tarefas_pendentes.append(nova_tarefa)
        print ('Tarefa adicionada com sucesso!')
        print('')

        #continuação ou não do processo
        retorno = retorno_processo()
        if not retorno:
            break


    #remove tarefa pendente             
    elif comando == 2:

        #imprime, em linhas diferentes, as tarefas pendentes
        for i in range(len(tarefas_pendentes)):
            print(i,'-',tarefas_pendentes[i])
        print('')

        #armazena a tarefa a ser removida
        escolha = int(input('Escolha o numero da tarefa a ser removida: '))
        print('')

        if escolha in range(len(tarefas_pendentes)):
            
            #remove a tarefa da lista de tarefas pendentes
            tarefas_pendentes.pop(escolha)
            print('Tarefa removida com sucesso!')
            print('')

            #continuação ou não do processo
            retorno = retorno_processo()
            if not retorno:
                break
        
        else:
            print('Numeração inválida.')
            print('')

            #continuação ou não do processo
            retorno = retorno_processo()
            if not retorno:
                break


    #imprime todas as tarefas pendentes
    elif comando == 3:

        #imprime, em linhas diferentes, as tarefas pendentes
        for i in range(len(tarefas_pendentes)):
            print(i,'-',tarefas_pendentes[i])
            
        print('')

        #continuação ou não do processo
        retorno = retorno_processo()
        if not retorno:
            break


    #imprime todas as tarefas concluidas
    elif comando == 4:

        #imprime, em linhas diferentes, as tarefas concluidas
        for i in range(len(tarefas_concluidas)):
            print(i,'-',tarefas_concluidas[i])
            print('')

        #continuação ou não do processo
        retorno = retorno_processo()
        if not retorno:
            break
 
    #conclui tarefa pendente
    elif comando == 5:

        #imprime, em linhas diferentes, as tarefas concluidas
        for i in range(len(tarefas_pendentes)):
            print(i,'-',tarefas_pendentes[i])

        #armazena a tarefa concluida
        escolha = int(input('Escolha o numero da tarefa concluida: '))
        print('')


        # remove a tarefa da lista de tarefas pendentes e adiciona a lista de tarefas concluidas
        if escolha in range(len(tarefas_pendentes)):
            tarefas_pendentes.pop(escolha)
            tarefas_concluidas.append(tarefas_pendentes[escolha])

            print('Tarefa concluida com sucesso!')
            print('')

            #continuação ou não do processo
            retorno = retorno_processo()
            if not retorno:
                break
        
        else:
            print('Numeração inválida.')
            print('')

            #continuação ou não do processo
            retorno = retorno_processo()
            if not retorno:
                break


    else:
        print('Numeração inválida.')
        print('')

        #continuação ou não do processo
        retorno = retorno_processo()
        if not retorno:
            break
    


