from functools import reduce

def sumatorio(lista):
    resultado = 0
    for numero in lista:
        resultado += numero
    return resultado

def sumatorioDoble(lista):
    resultado = 0
    for numero in lista:
        resultado += numero * 2
    return resultado

def producto(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

lista = [1,3,-1,15,9,2,8]

sumatorio = reduce(lambda x, y:x + y, lista)

# creo una copia de la lista
l = lista[:]
# añadimos un neutro para la suma en la posicion 0
l.insert(0,0)

sumatorioDobles = reduce(lambda x, y:x + y * 2, l)

print(sumatorio)
print(sumatorioDobles)