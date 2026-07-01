print('Escribe un numero mayor de 0 para saber que hora es en un reloj de 12 horas.')
num=int(input('Número: '))
res=num%12
if num<0:
     print('Error: El número debe ser mayor o igual a 0')
elif res==0:
     print('Hora: 12:00')
else:
     print(str(res)+':00')
enter=input('Presiona enter para salir.')