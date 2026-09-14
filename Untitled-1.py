valor_total = float(input("digite o valor total de sua compra:"))


def calcular_desconto(valor_total):
  if valor_total < 200:
    desconto = 0.05
    print("O desconto aplicado é de 5%")
  elif valor_total < 300:
    desconto = 0.10
    print("O desconto aplicado é de 10%")
  else:
    desconto = 0.15
    print("O desconto aplicado é de 15%")
  return desconto

desconto = calcular_desconto(valor_total)
valor_desconto = valor_total * desconto
valor_final = valor_total - valor_desconto
print("O valor final da compra é de: R$", valor_final)