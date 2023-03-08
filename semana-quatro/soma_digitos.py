numero = int(input("Digite um número inteiro:"))
soma = 0
resto = 0
count = 0

while (numero != 0):
    resto = numero % 10
    soma = soma + resto
    numero = numero // 10
    count = count + 1

print(soma)


