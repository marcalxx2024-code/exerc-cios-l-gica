nome_usuario = input("Qual é o seu nome? ")
print("Olá, " + nome_usuario + "! Bem-vindo ao programa.")
ano_nascimento = int(input("Em que ano você nasceu? "))
idade = 2026 - ano_nascimento
print("Você tem " + str(idade) + " anos.")
genero = input("Qual é o seu gênero? (M/F) ")
if genero.upper() == "M":
    print("Você é do gênero masculino.")
else:
    print("Você é do gênero feminino.")   
