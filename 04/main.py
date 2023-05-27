# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Resolução da Questão 4 de LPA
# Nome: Caio Detz - RU: 4315004
# Link Do Projeto: https://github.com/kard-py/LPA
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


print("""
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Bem Vindo ao Controle de Estoque da bicicletaria do Caio Detz
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")

# Database
db = []
# Contador para gerar os id
counter = 0


def cadastrarPeca(counter):
    # mostra algumas informações
    print("Você Selecionou a Opção Cadastar Peça")
    print(f"Codigo da Peça: {counter:0>4}")
    # Gera o id Unico
    id = f"{counter:0>4}"
    # pega os inputs
    nome = str(input("Por favor entre com o NOME Da Peça: "))
    fabricante = str(input("Por favor entre com o FABRICANTE Da Peça: "))
    valor = str(input("Por favor entre com o VALOR(R$) Da Peça: "))
    # Adiciona no banco de dados
    db.append({
        "id": id,
        "nome": nome,
        "fabricante": fabricante,
        "valor": valor
    })


def consultarPeca():
    print("Você Selecionou a Opção Consultar Peça")
    while True:
        print("Escolha a opção desejada:\n1 - Consultar Todas as Peças\n2 - Consultar Peças por Código\n3 - Consultar Peças por Fabricante\n4 - Retornar")
        op = str(input(">> "))
        if op == "1":
            for produto in db:
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                for key, value in produto.items():
                    print(f"{key}:{value}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        elif op == "2":
            id = str(input("Digite o Codigo do Produto: "))
            for produto in db:
                if produto["id"] == id:
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                    for key, value in produto.items():
                        print(f"{key}:{value}")
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        elif op == "3":
            
            fabricante = str(input("Digite o Fabricante do Produto: "))
            for produto in db:
                if produto["fabricante"] == fabricante:
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                    for key, value in produto.items():
                        print(f"{key}:{value}")
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        elif op == "4":
            break
        else:
            print("Opção Invalida")
            continue



def removerPeca():
    # pega o id por inputo do usuario
    id = str(input("Digite o codigo da peça a ser removida: "))
    for i in db:
        # verifica se o id é o mesmo do objeto
        if id == i["id"]:
            # Pega o Index do id a ser removido
            uid = db.index(i)
            # remove o id
            del db[uid]
            # para o loop
            print("Peça Removida com Sucesso! Voltando ao Menu")
            break
        else:
            continue


while True:
    print("Escolha a opção desejada:\n1 - Cadastrar Peças\n2 - Consultar Peças\n3 - Remover Peças\n4 - Sair")
    op = str(input(">> "))
    if op == "1":
        counter += 1
        cadastrarPeca(counter)
    elif op == "2":
        consultarPeca()
    elif op == "3":
        removerPeca()
    elif op == "4":
        break
    else:
        print("Opção Invalida")
        continue
