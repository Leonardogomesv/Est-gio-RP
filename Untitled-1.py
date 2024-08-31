def is_fibonacci(n):
    if n < 0:
        return False
    # Função para verificar se um número é quadrado perfeito
    def is_perfect_square(x):
        s = int(x**0.5)
        return s * s == x

    # Verifica se 5*n^2 + 4 ou 5*n^2 - 4 é um quadrado perfeito
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def main():
    try:
        num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    except ValueError:
        print("Por favor, informe um número inteiro válido.")
        return

    if is_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
