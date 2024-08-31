def count_a_in_string(s):
    # Conta a quantidade de letras 'a' ou 'A' na string
    count = s.lower().count('a')
    return count

def main():
    input_string = input("Informe uma string para contar a letra 'a': ")
    count = count_a_in_string(input_string)
    print(f"A letra 'a' ocorre {count} vez(es) na string.")

if __name__ == "__main__":
    main()
