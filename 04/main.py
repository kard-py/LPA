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


def cadastrarPeca(counter=counter, db=db):
    # Aumenta o Contador em 1
    counter += 1
    # mostra algumas informações
    print("Você Selecionou a Opção Cadastar Peça")
    print(f"Codigo da Peça: {counter:0>3}")
    # Gera o id Unico
    id = f"{counter:0>3}"
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


def consultarPeca(counter=counter, db=db):

    pass


def removerPeca(counter=counter, db=db):
    # pega o id por inputo do usuario
    id = str(input("Digite o codigo da peça a ser removida: "))
    print(db)
    for i in db:
        # verifica se o id é o mesmo do objeto
        if id == i["id"]:
            # Pega o Index do id a ser removido
            uid = db.index(i)
            # remove o id
            del db[uid]
            # para o loop

            print(db)
            break
        else:
            continue


while True:
    print("Escolha a opção desejada:\n1-Cadastrar Peças\n2-Consultar Peças\n3-Remover Peças\n4-Sair")
    op = str(input(">> "))
    if op == "1":
        cadastrarPeca()
    elif op == "2":
        consultarPeca()
    elif op == "3":
        removerPeca()
    elif op == "4":
        break
    else:
        print("Opção Invalida")
        continue
