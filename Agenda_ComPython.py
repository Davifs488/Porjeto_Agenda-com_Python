def menu():
    print(("\n Menu"))
    print("1. Adicionar contato")
    print("2. Buscar telefone por nome")
    print("3. Sair")
    return int(input(("Escolha uma opção: ")))


def adicionar_contato(agenda):
    nome = input("Digite o  nome : ")
    telefone = input("Digite o telefone :")
    agenda[nome] = telefone
    print(f"Contato {nome}  adicionado com sucesso !")


def buscar_telefone(agenda):
        nome = input(("Digite o nome para buscar o telefone : "))
        if nome in agenda:
            print(f"Telefone de {nome} : {agenda[nome]}")
        else:
            print("Contato não encontrado !")

def main():
    agenda = {}
    while True:
        opcao = menu()
        if opcao == 1:
            adicionar_contato(agenda)
        elif opcao == 2:
             buscar_telefone(agenda)
        elif opcao == 3:
             print("Opçãoa inválida ! ")
             break
        else:
             print("Opção iválida")

if __name__ == "__main__" :
    main()
