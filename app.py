#Atividade registro de entrada do cinema

nome = input("Informe o nome: ")
idade = int(input("Informe a idade: "))

#salas, inicio do loop
while True:
    print("Sala 1 - Carros - Livre")
    print("Sala 2 - Batman - 12 anos")
    print("Sala 3 - Homem de Ferro - 14 anos")
    print("Sala 4 - Vingadores - 16 anos")
    print("Sala 5 - Deadpool - 18 anos")
    sala = input("Informe a sala desejada: ")

# estrutura de decisão 
    match sala:
        case "1":
            idade_minima = 0
        case "2":
            idade_minima = 12
        case "3":
            idade_minima = 14
        case "4":
            idade_minima = 16
        case "5":
            idade_minima = 18
        # default (valor inválido)
        case _:
            print("Sala inexistente.")    
            continue
# vai fazer a verificação da idade do usuário 
    if idade >= idade_minima:
        print(f"Entrada de {nome} autorizada. Tenha bom filme!!!")
        break
    else:
        print(f"Entrada de {nome} não autorizada")  
        print(f"{nome} Por favor escolher outro filme.")
        continue