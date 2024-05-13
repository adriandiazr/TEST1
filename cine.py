filas = 10
columnas = 10
arreglo_asientos = []2

def crear_arreglo():
    for f in range(filas):
        arreglo_pro = []
        for c in range(columnas):
            arreglo_pro.append('.')
        arreglo_asientos.append(arreglo_pro)

def imprimir():
    numero_asiento = 1
    for fila in arreglo_asientos:
        # print(fila)
        for columna in fila:
            if columna == 'X':
                print('X', end=" ")
            else:
                print(numero_asiento, end=" ")
            numero_asiento = numero_asiento + 1
        print('')

def buscar_asiento(asiento):
    numero_asiento = 1
    for n_f, fila in enumerate(arreglo_asientos):
        for n_c, columna in enumerate(fila):
            if (numero_asiento == asiento):
                if arreglo_asientos[n_f][n_c] == 'X':
                    print('Error el asiento ya esta reservado')
                else:
                    arreglo_asientos[n_f][n_c] = 'X'
            numero_asiento = numero_asiento + 1

crear_arreglo()
imprimir()
print('\n\n')
buscar_asiento(10)
imprimir()
buscar_asiento(11)
imprimir()
buscar_asiento(10)

# print(arreglo_asientos)
while True:
    try:
        cantidad_entradas = int(input('Ingrese la cantidad de entradas [1,3]: '))
        if cantidad_entradas >= 1 and cantidad_entradas <= 3:
            break
        else:
            print('no son los valores de 1 2 o 3 entradas ')
    except:
        print('ingrese nuevamente')


