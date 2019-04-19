def maximo(*l):
    if len(l) == 0:
        return 0
    maximo = l[0]
    for numero in range(1, len(l)):
        if l[numero] > maximo:
            maximo = l[numero]
    return maximo

def minimo(*l):
    if len(l) == 0:
        return 0
    minimo = l[0]
    for numero in range(1, len(l)):
        if l[numero] < minimo:
            minimo = l[numero]
    return minimo

def media(*l):
    if len(l) == 0:
        return 0
    suma = 0
    for numero in l:
        suma += numero
    return suma / len(l)
   
funciones = {
    'maximo':maximo,
    'minimo':minimo,
    'media':media}
   
def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    return None
        