# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Resolução da Questão 3 de LPA
# Nome: Caio Detz - RU: 4315004
# Link Do Projeto: https://github.com/kard-py/LPA
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Indentificador
print("""
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Bem Vindo a companhia de logistica Caio Detz S.A.
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")


def dimensoesObjeto():
    while True:
        try:
            comprimento = float(
                input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
            altura = float(input("Digite a altura do objeto (em cm): "))
            volume = altura * largura * comprimento
            print(f"Volume do objeto é (em cm³): {volume}")

            if volume < 1000:
                valor = int(10)
                return valor
            elif volume >= 1000 and volume < 10000:
                valor = int(20)
                return valor
            elif volume >= 10000 and volume < 30000:
                valor = int(30)
                return valor
            elif volume >= 30000 and volume < 100000:
                valor = int(50)
                return valor
            elif volume >= 100000:
                raise TypeError("Valor Muito Alto")
        except ValueError:
            print("Você digitou alguma dimensão do objeto em valor não numerico")
            print("Por favor entre com as dimensões desejadas novamente")
            continue
        except TypeError:
            print("Não aceitamos objetos com as dimenções tão grandes")
            print("Por favor entre com as dimensões desejadas novamente")
            continue


def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            if peso < 0.1:
                multiplicador = float(1.0)
                return multiplicador
            elif peso >= 0.1 and peso < 1:
                multiplicador = float(1.5)
                return multiplicador
            elif peso >= 1 and peso < 10:
                multiplicador = float(2.0)
                return multiplicador
            elif peso >= 10 and peso < 30:
                multiplicador = float(3.0)
                return multiplicador
            elif peso >= 30:
                raise TypeError("Valor Muito Alto")
        except ValueError:
            print("Você digitou o peso do objeto em valor não numerico")
            print("Por favor entre com as dimensões desejadas novamente")
            continue
        except TypeError:
            print("Não aceitamos objetos tão pesados")
            print("Por favor entre com as dimensões desejadas novamente")
            continue


def rotaObjeto():
    while True:
        print("Selecione a rota:")
        print("""RS - De Rio de Janeiro até São Paulo\nSR - De São Paulo até Rio de Janeiro\nBS - De Brasília até São Paulo\nSB - De São Paulo até Brasília\nBR - De Brasília até Rio de Janeiro\nRB - Rio de Janeiro até Brasília\n""")
        sigla = str(input(">> ")).upper()
        if sigla == "RS":
            multiplicador = float(1)
            return multiplicador
        elif sigla == "SR":
            multiplicador = float(1)
            return multiplicador
        elif sigla == "BS":
            multiplicador = float(1.2)
            return multiplicador
        elif sigla == "SB":
            multiplicador = float(1.2)
            return multiplicador
        elif sigla == "BR":
            multiplicador = float(1.5)
            return multiplicador
        elif sigla == "RB":
            multiplicador = float(1.5)
            return multiplicador
        else:
            print("Você digitou uma rota que não existe")
            continue


# Chama As Funcções e pega os valores
valor = dimensoesObjeto()
multiplicadorPeso = pesoObjeto()
multiplicadorRota = rotaObjeto()

# Caucula o Total
total = (valor * multiplicadorPeso) * multiplicadorRota
print(
    f"Total a pagar(R$): {total:.2f} (dimensões: {valor} * peso: {multiplicadorPeso} * rota: {multiplicadorRota})")
