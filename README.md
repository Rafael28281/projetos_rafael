# Projetos de Consumo e Desconto

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-181717?logo=github&logoColor=white)
![Agua](https://img.shields.io/badge/%C3%81gua-Consumo-2196F3?logo=water&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-Economia-F4B400?logo=flash&logoColor=white)

## Objetivo do sistema

Este projeto reúne dois programas simples em Python para praticar entrada de dados, regras condicionais e cálculos:

- `consumoAgua.py`: classifica o consumo mensal de água de acordo com o tipo de imóvel e orienta sobre economia e possíveis vazamentos.
- `DescontoCompra.py`: calcula o desconto progressivo e o valor final de uma compra.

## Linguagem utilizada

- **Python 3.10 ou superior**

Não há dependências externas. Basta ter o Python instalado.

## Como executar

1. Clone o repositório e entre na pasta do projeto:

	```bash
	git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
	cd SEU_REPOSITORIO
	```

2. Execute o programa de consumo de água:

	```bash
	python consumoAgua.py
	```

	Informe o tipo de imóvel (`comercial`, `casa` ou `apartamento`) e o consumo mensal em m³.

3. Execute o programa de desconto:

	```bash
	python DescontoCompra.py
	```

	Informe o valor total da compra para receber o desconto e o valor final.

No Windows, caso o comando `python` não funcione, tente usar `py`:

```powershell
py consumoAgua.py
py DescontoCompra.py
```

## Regras de desconto

| Valor da compra | Desconto |
|---|---:|
| Menor que R$ 200,00 | 5% |
| De R$ 200,00 a menos de R$ 300,00 | 10% |
| R$ 300,00 ou mais | 15% |

## Estrutura do projeto

```text
.
├── consumoAgua.py
├── DescontoCompra.py
└── README.md
```
