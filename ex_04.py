dados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

def calculate_universe():
    return sum(dados.values())

def calculate_percentage_participation(dado):
    values_universe = calculate_universe()
    percentage = (dados[dado]/values_universe)*100
    return f'"{dado}": {percentage:.2f}%'

for dado in dados:
    print(calculate_percentage_participation(dado))