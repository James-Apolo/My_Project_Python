
'''*********** ORGANIZADOR DE TAREFAS  **************


* TÍLULO: Organizador de Tarefas
*AUTOR: [JAMES_ALCON]
*DATA: 2026-01-26
*DESCRIÇÂO: Algoritmo para organizar tarefas, onde você pode adicionar, listar e concluir tarefas.
*CONCEITOS: - Listas para armazenar tarefas
            - Dicionários para representar cada tarefa com id, descrição e estado
            
**************************************************'''



#Adiciona uma nova tarefa com estado 'Pendente' e id incremental.
def add_tarefa(lista, descricao):
    if lista:
        novo_id = lista[-1]['id'] + 1

    else:
        novo_id = 1
    tarefa = {"id": novo_id, "descricao": descricao, "estado": "Pendente"}
    lista.append(tarefa)
    print("Tarefa adicionada.")

#Mostra todas as tarefas ou avisa se a lista estiver vazia.
def listar_tarefas(lista):
    if not lista:
        print("A lista de tarefas está vazia.")
        return
    
    print("--- AS MINHAS TAREFAS ---")
    for tarefa in lista:
        print(f"[{tarefa['id']}] {tarefa['descricao']} - ({tarefa['estado']})")

#Muda o estado da tarefa de 'Pendente' para 'Concluída' pelo ID.
def concluir_tarefa(lista, id_tarefa):
    for tarefa in lista:
        if tarefa['id'] == id_tarefa:
            if tarefa['estado'] == "Pendente":
                tarefa['estado'] = "Concluída"
                print(f"Tarefa {id_tarefa} concluída.")
            else:
                print(f"A tarefa {id_tarefa} já está concluída.")
            return
    print(f"Tarefa com ID {id_tarefa} não encontrada.")

#Menu do programa.
def menu():
    tarefas = []
    while True:
        print("\n=== TO-DO LIST v1.0 ===")
        print("1. Adicionar")
        print("2. Listar")
        print("3. Concluir")
        print("0. Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            descricao = input("Descrição da tarefa: ").strip()
            if descricao:
                add_tarefa(tarefas, descricao)

            else:
                print("Descrição inválida. Tente novamente.")

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            try:
                id_tarefa = int(input("ID da tarefa a concluir: ").strip())
                concluir_tarefa(tarefas, id_tarefa)
            except ValueError:
                print("ID inválido. Por favor, insira um número inteiro.")

        elif opcao == "0":
            print("A sair do programa.")
            break

        else:
            print("Opção inválida.Escolha entre 0 e 3.")

if __name__ == "__main__":
    menu()
