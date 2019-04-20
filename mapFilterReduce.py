from functools import reduce

def doble(numero):
    return numero * 2

def pares(numero):
    # otra opcion seria simplemente poner return x % 2 == 0
    if numero % 2 == 0:
        return numero
    else:
        return None

lista = [1,3,-1,15,9,2,8]

listaDobles = map(lambda x:x * 2, lista) # map aplica en este caso lo que le pedimos a la funcion lambda a todos los elementos
                                         # de la lista

listaDobles1 = map(doble, lista)

listaPares = filter(lambda x:x % 2 == 0, lista) # filter filtra todos los elementos de una lista por ej en base a una condicion que
                                                # le pedimos en este caso utilizando una funcion lambda
                                                
listaPares1 = filter(pares, lista)                                                

sumatorio = reduce(lambda x, y:x + y, lista) # reduce lo que hace es nos devuelve un solo valor a partir de una lista, etc y en este
                                             # caso la funcion lambda tiene 2 parametros x que es el que comienza vacio y va almace
                                             # nando los valores seria el acumulador e y que es el que va iterando por la lista
                                             
suma100 = reduce(lambda x, y:x + y, range(101))                                             
sumatorioDobles = reduce(lambda x, y:x + y * 2, lista)

