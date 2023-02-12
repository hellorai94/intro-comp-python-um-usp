segundosStr = input("Digite o número de segundos: ")
intSegundos = int(segundosStr)

horasSegundos = intSegundos // 3600
segundosResto = intSegundos % 3600
segundosMin = segundosResto // 60
segundosFinal = segundosResto % 60

print(horasSegundos,"horas,", segundosMin, "minutos e", segundosFinal,"segundos.")

