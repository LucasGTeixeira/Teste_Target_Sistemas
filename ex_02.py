def fibonacci_sequence(n):
    #inicio da sequencia
    sequence = [0, 1]
    #enquanto o ultimo termo da sequencia for menor que o falor inserido
    while sequence[-1] < n:
        #soma o ultimo valor da sequencia com seu antecessor
        next_number = sequence[-1] + sequence[-2]
        #adiciona a soma como ultimo elemento da lista
        sequence.append(next_number)
    return sequence

def main():
    # Recebe o numero a ser encontrado na sequencia
    n = int(input("Digite um número: "))

    # Calcula a sequência de Fibonacci até o número n
    sequence = fibonacci_sequence(n)

    # Verifica se o número está presente na sequência
    if n in sequence:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()