import json

with open("ex_03/dados.json") as f:
    dados = json.load(f)

def extract_revenue_from_list(data_list):
    revenue = [dado['valor'] for dado in data_list]
    return revenue

def calculate_higher_billing(billing_list):
    return max(billing_list)

def calculate_lower_billing(billing_list):
    return min(billing_list)

def calculate_monthly_average(billing_list):
    billing_sum = sum(billing_list)
    days = len(billing_list)
    return billing_sum/days

def calculate_above_average_billings(billing_list):
    billing_average = calculate_monthly_average(billing_list)
    days_above_average = sum(1 for bill in billing_list if bill > billing_average)
    return days_above_average

billing_list = extract_revenue_from_list(dados)

print(f'Maior faturamento: {calculate_higher_billing(billing_list):.2f}')
print(f'Menor faturamento: {calculate_lower_billing(billing_list)}')
print(f'Média de faturamento do mês: {calculate_monthly_average(billing_list):.2f}')
print(f'Número de dias acima da média do faturamento mensal: {calculate_above_average_billings(billing_list)}')
