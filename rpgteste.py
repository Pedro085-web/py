# MODO TESTE

nome = input("Digite seu nome")
classe = "Guerreiro"
hp=100
print("=== MODO DE TESTE ===")
print("Nome:", nome)
print("Classe:", classe)

input(" -> ENTER <- ")

print("Capítulo 01: O chamado")

input(" -> ENTER <- ")

print("Você está em uma missão de salvar a princesa Ellie das mãos de um rei tirano.")

input(" -> ENTER <- ")

print("Você está caminhando pela floresta quando então...")

input(" -> ENTER <- ")

print("Uma moça segurando uma flauta aparece correndo em sua direção.")

input(" -> ENTER <- ")

print("Moça Desconhecida: Você, me ajude por favor!!!!")

input(" -> ENTER <- ")

print("[1] O que houve?")
print("[2] Não me atrapalhe")
print("[3] Não respondo nada")

resposta = input("Qual é a sua resposta? ")

if resposta == "1":
    print("Graças a Oghma uma boa alma!")

elif resposta == "2":
    print("Eu te imploro, por favor!")

elif resposta == "3":
    print("To falando com voce me ajuda.")

else:
    print("Lyra não entendeu sua resposta.")

input(" -> ENTER <- ")

print("Me chamo Lyra. Estou em busca de um viajante chamado", nome)

input(" -> ENTER <- ")

print("É você?")

input(" -> ENTER <- ")

print("[1] Sim, sou eu mesmo!")
print("[2] Por que o está procurando?")
print("[3] E se eu for, hein?")

resposta2 = input("Qual é a sua resposta? ")

if resposta2 == "1":
    print("Excelente! Tenho uma mensagem do Rei para você.")

elif resposta2 == "2":
    print("Tenho uma mensagem para ele.")

elif resposta2 == "3":
    print("Calma! Eu não sou uma inimiga.")

else:
    print("Lyra não entendeu sua resposta.")
