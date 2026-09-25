print("=== SISTEMA DE VOTO ===")

nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")

input(f"\nOlá, {nome}! Pressione ENTER para prosseguir.")

votar = input("[1] Candidato A\n[2] Candidato B\nEscolha seu candidato: ")

if votar == "1":
    print(f"\n{nome}, você votou no Candidato A.")
elif votar == "2":
    print(f"\n{nome}, você votou no Candidato B.")
else:
    print("\nOpção inválida.")



