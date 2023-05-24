# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Resolução da Questão 2 de LPA
# Nome: Caio Detz - RU: 4315004
# Link Do Projeto: https://github.com/kard-py/LPA
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Tabela de Produtos
produtos = {
    "100": {
        "nome": "Cachorro-Quente",
        "valor": 9.00
    },
    "101": {
        "nome": "Cachorro-Quente Duplo",
        "valor": 11.00
    },
    "102": {
        "nome": "X-Egg",
        "valor": 12.00
    },
    "103": {
        "nome": "X-Salada",
        "valor": 13.00
    },
    "104": {
        "nome": "X-Bacon",
        "valor": 14.00
    },
    "105": {
        "nome": "X-Tudo",
        "valor": 17.00
    },
    "200": {
        "nome": "Refrigerante Lata",
        "valor": 5.00
    },
    "201": {
        "nome": "Chá Gelado",
        "valor": 4.00
    },
}

# indentificador
print("""
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Bem Vindo a Lanchonete do Caio Detz
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")

# lista de pedidos
pedidos = []

while True:
    cod = str(input("Entre com o código desejado: "))
    if cod == "100":
        print(
            f"Você pediu um {produtos[cod]['nome']} no valor de {produtos[cod]['valor']:.2f}")
        pedidos.append(produtos[cod])
        print("Deseja pedir mais alguma coisa?\n[1] - Sim\n[0] - Não")
        op = str(input(">> "))
        if (op == "1"):
            continue
        elif (op == "0"):
            break
    elif cod == "101":

        print(
            f"Você pediu um {produtos[cod]['nome']} no valor de {produtos[cod]['valor']:.2f}")
        pedidos.append(produtos[cod])
        print("Deseja pedir mais alguma coisa?\n[1] - Sim\n[0] - Não")
        op = str(input(">> "))
        if (op == "1"):
            continue
        elif (op == "0"):
            break
    elif cod == "102":
        print(
            f"Você pediu um {produtos[cod]['nome']} no valor de {produtos[cod]['valor']:.2f}")
        pedidos.append(produtos[cod])
        print("Deseja pedir mais alguma coisa?\n[1] - Sim\n[0] - Não")
        op = str(input(">>"))
        if (op == "1"):
            continue
        elif (op == "0"):
            break
    elif cod == "103":
        print(
            f"Você pediu um {produtos[cod]['nome']} no valor de {produtos[cod]['valor']:.2f}")
        pedidos.append(produtos[cod])
        print("Deseja pedir mais alguma coisa?\n[1] - Sim\n[0] - Não")
        op = str(input(">> "))
        if (op == "1"):
            continue
        elif (op == "0"):
            break
    elif cod == "104":
        print(
            f"Você pediu um {produtos[cod]['nome']} no valor de {produtos[cod]['valor']:.2f}")
        pedidos.append(produtos[cod])
        print("Deseja pedir mais alguma coisa?\n[1] - Sim\n[0] - Não")
        op = str(input(">> "))
        if (op == "1"):
            continue
        elif (op == "0"):
            break
    elif cod == "105":
        print(
            f"Você pediu um {produtos[cod]['nome']} no valor de {produtos[cod]['valor']:.2f}")
        pedidos.append(produtos[cod])
        print("Deseja pedir mais alguma coisa?\n[1] - Sim\n[0] - Não")
        op = str(input(">> "))
        if (op == "1"):
            continue
        elif (op == "0"):
            break
    elif cod == "200":
        print(
            f"Você pediu um {produtos[cod]['nome']} no valor de {produtos[cod]['valor']:.2f}")
        pedidos.append(produtos[cod])
        print("Deseja pedir mais alguma coisa?\n[1] - Sim\n[0] - Não")
        op = str(input(">> "))
        if (op == "1"):
            continue
        elif (op == "0"):
            break
    elif cod == "201":
        print(
            f"Você pediu um {produtos[cod]['nome']} no valor de {produtos[cod]['valor']:.2f}")
        pedidos.append(produtos[cod])
        print("Deseja pedir mais alguma coisa?\n[1] - Sim\n[0] - Não")
        op = str(input(">> "))
        if (op == "1"):
            continue
        elif (op == "0"):
            break
    else:
        print("Opção Invalida")
        continue

# caucula o total
total = 0
for p in pedidos:
    total += p['valor']
# Exibe o total
print(f"O Total a ser pago é: {total:.2f}")
