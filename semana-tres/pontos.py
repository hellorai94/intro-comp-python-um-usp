import math

xUm = float(input("Coordenada X - Primeiro Plano:"))
xDois = float(input("Coordenada Y - Primeiro Plano:"))
yUm = float(input("Coordenada X - Segundo Plano:"))
yDois = float(input("Coordenada Y - Segundo Plano:"))

formula = (((xUm - xDois) ** 2) + ((yUm - yDois) ** 2))
raiz = math.sqrt(formula)
print(raiz)

if (raiz >= 10):
    print("longe")
else:
    print("perto")
