import math

a = float(input("Digite a:"))
b = float(input("Digite b:"))
c = float(input("Digite c:"))

delta = ((b ** 2) - 4 * a * c)


if delta == 0:
    xUm = ((- b + math.sqrt(delta)) / (2 * a))
    print("a raiz desta equação é",xUm)
elif delta > 0:
    xUm = ((- b + math.sqrt(delta)) / (2 * a))
    xDois = ((- b - math.sqrt(delta)) / (2 * a))
    if xUm < xDois:
        print("as raízes da equação são",xUm,"e",xDois,".")
    else:
        print("as raízes da equação são",xDois,"e",xUm,".")
else:
     print("esta equação não possui raízes reais")
    
