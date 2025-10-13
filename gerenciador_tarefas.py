tarefas = []

def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso")
    return 

def ver_tarefas(tarefas):
    print("Lista de tarefas:\n", tarefas)
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "X" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice inválido")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["completada"] = True
        print("Tarefa completada")
    else:
        print("Indice inválido")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"] == True:
            tarefas.remove(tarefa)
    print("Tarefa deletada")
    return

while True:
    print("MENU")
    print("1 - ADICIONAR TAREFA")
    print("2 - VER TAREFAS")
    print("3 - ATUALIZAR TAREFAS")
    print("4 - COMPLETAR TAREFA")
    print("5 - DELETAR TAREFA COMPLETADA")
    print("6 - SAIR")
    
    escolha = input("DIGITE SUA ESCOLHA: ")
    if escolha == "1":
       nome_tarefa = input("Qual o nome da tarefa que deseja adicionar: ")
       adicionar_tarefa(tarefas, nome_tarefa)
       
    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o indice da tarefa: ")
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
    
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o indice da tarefa completada: ")
        completar_tarefa(tarefas, indice_tarefa)
    
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == "6":
        break

print("Programa finalizado")