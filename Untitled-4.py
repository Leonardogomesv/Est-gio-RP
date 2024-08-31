def next_odd_number(sequence):
    return sequence[-1] + 2

sequence_a = [1, 3, 5, 7]
print(f"Próximo número na sequência a) é {next_odd_number(sequence_a)}")

def next_power_of_two(sequence):
    return sequence[-1] * 2

sequence_b = [2, 4, 8, 16, 32, 64]
print(f"Próximo número na sequência b) é {next_power_of_two(sequence_b)}")

def next_square_number(sequence):
    n = int(sequence[-1]**0.5) + 1
    return n * n

sequence_c = [0, 1, 4, 9, 16, 25, 36]
print(f"Próximo número na sequência c) é {next_square_number(sequence_c)}")

def next_even_square(sequence):
    n = int(sequence[-1]**0.5) + 2
    return n * n

sequence_d = [4, 16, 36, 64]
print(f"Próximo número na sequência d) é {next_even_square(sequence_d)}")

def next_fibonacci(sequence):
    return sequence[-1] + sequence[-2]

sequence_e = [1, 1, 2, 3, 5, 8]
print(f"Próximo número na sequência e) é {next_fibonacci(sequence_e)}")

def next_in_sequence(sequence):
    return sequence[-1] + 1

sequence_f = [2, 10, 12, 16, 17, 18, 19]
print(f"Próximo número na sequência f) é {next_in_sequence(sequence_f)}")

