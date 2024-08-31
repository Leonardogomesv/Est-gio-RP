import random
import time

# Função para simular o estado das lâmpadas
def initialize_lights():
    # Simula quais interruptores controlam quais lâmpadas
    lights = {1: None, 2: None, 3: None}
    switches = [1, 2, 3]
    random.shuffle(switches)
    for i, switch in enumerate(switches, 1):
        lights[switch] = f"Lâmpada {i}"
    return lights

# Função para simular a interação com os interruptores e lâmpadas
def simulate_switches_and_lights(lights):
    # Estado dos interruptores
    state = {1: 'desligado', 2: 'desligado', 3: 'desligado'}
    
    # 1ª Ida - Liga o primeiro interruptor e espera
    state[1] = 'ligado'
    print("Ligando o Interruptor 1 e esperando...")
    time.sleep(10)  # Espera simulada (10 segundos)

    # Desliga o primeiro interruptor e liga o segundo interruptor
    state[1] = 'desligado'
    state[2] = 'ligado'
    print("Desligando o Interruptor 1 e ligando o Interruptor 2.")

    # 2ª Ida - Simula a verificação das lâmpadas
    print("Segunda ida para verificar as lâmpadas...")
    results = {}
    for i in range(1, 4):
        lamp = lights[i]
        if state[i] == 'ligado':
            results[lamp] = 'Acesa'
        else:
            results[lamp] = 'Desligada e Fria'
    
    return results

def main():
    lights = initialize_lights()
    print("Estado das lâmpadas (não visível):")
    for switch, lamp in lights.items():
        print(f"Interruptor {switch} -> {lamp}")

    results = simulate_switches_and_lights(lights)
    
    print("\nResultado da Segunda Ida:")
    for lamp, status in results.items():
        print(f"{lamp} está {status}")

if __name__ == "__main__":
    main()
