#Datos constantes
IVA = 0.19
RECARGO= 0.5
#Solicitud de precio base
precio_base = float(input('Ingrese el precio base del producto:'))
#Validacion de precio
if precio_base <= 0:
    print('Error: Valor inválido.')
else:
    #Solicitar código de categoría
    print('Categoría de producto:')
    print('1) Producto básico.')
    print('2) Producto estándar.')
    print('3) Producto de lujo.')
    codigo_categoria = int(input('Digite el número de la categoría:'))
    #Calcular y mostrar el valor final según la categoría de lo contrario mostrar error.
    if codigo_categoria < 1 or codigo_categoria >3:
        print('Error: Valor inválido.')
    else:
        if codigo_categoria == 1:
            valor_final = precio_base
        elif codigo_categoria == 2:
            valor_final = precio_base + precio_base * IVA
        else:
            valor_final = precio_base + precio_base * IVA + precio_base * RECARGO
        print(f'Valor final = {valor_final}')