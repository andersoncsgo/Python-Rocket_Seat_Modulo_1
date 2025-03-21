def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}    
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionado com sucesso")

    return


tarefas = []
while True:
    print("Menu do Gerenciador de lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. ver tarefas")
    print("3. atualizar tarefa")
    print("4. completa tarefa")
    print("6. deletar tarefas completadas")
    print("6. sair")
    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "6":
        break

print("Programa finalizado")
