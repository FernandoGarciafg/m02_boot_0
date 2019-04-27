# la recursividad es una funcion que para repetirse se invoca a si misma, una funcion es recursiva si para definirse se necesita
# solo a si misma y se llama a si misma, la recursividad tiene que tener una condicion de parada

def retroContador(numero):
    print("{}\n".format(numero), end = "")
    if numero > 0:
        retroContador(numero - 1)
            
def retroContador2(numero):
    if numero > 0:
        print("{}\n".format(numero), end = "")
        while numero > 0:
            (retroContador2(numero - 1))
            return numero
    else:
        pass

        
def sumatorio(numero):
    if numero < 0:
        pass
    elif numero != 0:
        return numero + sumatorio(numero - 1)
    else:
        return 0
    
def sumatorio2(numero):
    while numero > 0:
        return numero + sumatorio(numero - 1)
    return numero
        
def factorial(numero):
    contador = 1
    while contador != numero:
        contador += 1
        return numero * factorial(numero - 1)
    return numero

def factorial(numero):
    if numero > 1:
        contador = 1
        while contador != numero:
            contador += 1
            return numero * factorial(numero - 1)
    elif numero == 0 or numero == 1:
        return 1
    return

def factorial2(numero):
    if numero > 1:
        return numero * factorial(numero -1)
    elif numero == 0 or numero == 1:
        return 1
    return
        
#retroContador(10)
#retroContador2(10)
    
#print(sumatorio(12))
#print(sumatorio2(12))