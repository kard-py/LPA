# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Resolução da Questão 1 de LPA
# Nome: Caio Detz - RU: 4315004
# Link Do Projeto: https://github.com/kard-py/LPA
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


print("""
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Bem Vindo a Loja do Caio Detz
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")


valor = float(input("Entre com o valor do produto: "))
quantidade = int(input("Entre com a quantidade do produto: "))
if quantidade <= 0:
    print("Quantidade Invalida (Você não pode Comprar 0 Produtos).")
elif quantidade > 0 and quantidade <= 9:
    desconto = 0
elif quantidade >= 10 and quantidade <= 99:
    desconto = 5
elif quantidade >= 100 and quantidade <= 999:
    desconto = 10
elif quantidade > 1000:
    desconto = 15

valor = valor*quantidade

valor_com_desconto = valor - ((desconto/100) * valor)

print(f"O Valor sem desconto foi: R${valor:.2f}")
print(f"O Valor com desconto foi: R${valor_com_desconto:.2f} (Desconto de {desconto}%)")
