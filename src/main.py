

### Ficheiro `src/main.py`
###Crie o ficheiro `main.py` dentro da pasta `src/` e cole o código abaixo. Ele contempla **todas as regras de negócio do seu PDF da Fase 1** (validações de título e prioridade) e atende aos **requisitos da Fase 2** (campos de status e data limite).```python
"""
TaskTracker - Sistema de Gerenciamento de Tarefas (CLI)
Autor: Gabriel Pereira Melo dos Santos
Bootcamp II - Fase 2 (Etapa Intermediária)
"""

def exibir_menu():
    print("\n" + "=" * 40)
    print("        TASKTRACKER - MENU PRINCIPAL        ")
    print("=" * 40)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("=" * 40)


def cadastrar_tarefa(lista_tarefas):
    print("\n--- CADASTRO DE NOVA TAREFA ---")
    
    # 1. Validação do Título (Campo obrigatório)
    while True:
        titulo = input("Título da tarefa (obrigatório): ").strip()
        if titulo:
            break
        print(" Erro: O título é obrigatório e não pode ficar em branco!")

    # 2. Descrição (Opcional/Texto livre)
    descricao = input("Descrição da tarefa (opcional): ").strip()
    if not descricao:
        descricao = "Sem descrição"

    # 3. Validação da Prioridade (Alta, Média/Media, Baixa)
    prioridades_validas = {
        "ALTA": "Alta",
        "MÉDIA": "Média",
        "MEDIA": "Média",
        "BAIXA": "Baixa"
    }
    
    while True:
        prioridade_input = input("Prioridade (Alta, Média, Baixa): ").strip().upper()
        if prioridade_input in prioridades_validas:
            prioridade = prioridades_validas[prioridade_input]
            break
        print(" Erro: Prioridade inválida! Digite apenas 'Alta', 'Média' ou 'Baixa'.")

    # 4. Data Limite
    data_limite = input("Data limite (ex: DD/MM/AAAA ou informe livremente): ").strip()
    if not data_limite:
        data_limite = "Não informada"

    # 5. Criação do dicionário da tarefa com Status 'Pendente' por padrão
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    lista_tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas(lista_tarefas):
    print("\n--- LISTA DE TAREFAS CADASTRADAS ---")
    
    if not lista_tarefas:
        print(" Nenhuma tarefa cadastrada no momento.")
        return

    for idx, tarefa in enumerate(lista_tarefas, start=1):
        print(f"\n[ Tarefa #{idx} ]")
        print(f"  • Título:      {tarefa['titulo']}")
        print(f"  • Descrição:   {tarefa['descricao']}")
        print(f"  • Prioridade:  {tarefa['prioridade']}")
        print(f"  • Data Limite: {tarefa['data_limite']}")
        print(f"  • Status:      {tarefa['status']}")
        print("-" * 35)


def main():
    tarefas = []
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker... Até logo!")
            break
        else:
            print(" Opção inválida! Por favor, escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()