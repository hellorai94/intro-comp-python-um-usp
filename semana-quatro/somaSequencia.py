x = int(input("Digite uma sequência:"))
soma = 0
resto = 0

while (x != 0):
    resto = x % 10
    x = x // 10
    soma = soma + resto
    

print("A soma de todos números é:", soma)
