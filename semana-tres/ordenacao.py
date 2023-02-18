numUm = int(input("Digite o primeiro número:"))
numDois = int(input("Digite o segundo número:"))
numTres = int(input("Digite o terceiro número:"))

if (numUm < numDois) and (numDois < numTres):
    print("crescente")
else:
    print("não está em ordem crescente")
