segundosStr = input("Digite o número de segundos: ")
intSegundos = int(segundosStr)

diasSegundos = intSegundos // 86400
diasResto = intSegundos % 86400
horasSegundos = diasResto // 3600
horaResto = diasResto % 3600
minSegundos = horaResto // 60
minResto = horaResto % 60

print(diasSegundos,"dias,",horasSegundos,"horas,",minSegundos, "minutos e",minResto,"segundos.")

