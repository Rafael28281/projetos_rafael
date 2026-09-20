
# 1) Tipo de imóvel
tipo = input("Informe o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

# 2) Consumo mensal em m³
consumo = float(input("Informe o consumo mensal de água (m³): ").replace(",", "."))

# 3) Classificação conforme as regras de negócio
match tipo:
    case "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")

    case "apartamento" if consumo < 10:
        print("Consumo econômico – excelente controle de água!")

    case "apartamento":
        print("Consumo moderado – dentro do padrão residencial.")

    case "casa" if consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")

    case _:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

# 1) Tipo de imóvel
tipo = input("Informe o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

# 2) Consumo mensal em m³
consumo = float(input("Informe o consumo mensal de água (m³): ").replace(",", "."))

# 3) Classificação conforme as regras de negócio
match tipo:
    case "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")

    case "apartamento" if consumo < 10:
        print("Consumo econômico – excelente controle de água!")

    case "apartamento":
        print("Consumo moderado – dentro do padrão residencial.")

    case "casa" if consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")

    case _:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")