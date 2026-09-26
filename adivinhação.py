import random

print("=== SIMULADOR DE APOSTA ===")

while True:

    print("\nEscolha um número de 1 a 10")
    escolha = input("Sua escolha: ")

    resultado = random.randint(1, 10)

    if escolha == str(resultado):
        print("Você acertou!")
    else:
        print("Você errou!")
        print(f"O número sorteado foi {resultado}")

    continuar = input("\nDeseja jogar novamente? [s/n]: ")

    if continuar == "n":
        print("Obrigado por jogar!")
        break