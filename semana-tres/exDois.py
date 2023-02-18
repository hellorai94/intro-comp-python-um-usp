quant = int(input("Digite a quantidade de números:"))
cont = 0
somaPar = 0
somaImpar = 0

while (cont < quant):
    numero = int(input("Digite o número:"))
    cont = cont + 1
    if (numero % 2 == 0):
        somaPar = somaPar + 1
    else:
        somaImpar = somaImpar + 1
        
print("Quantidade de número par:",somaPar,".")
print("Quantidade de número ímpar:",somaImpar,".")
