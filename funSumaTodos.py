def sumaTodos(limite):
    resultado = 0
    for i in range(0, limite + 1):
        resultado += i
    
    return resultado

def sumaLosCuadrados(limite):
    resultado = 0
    for i in range(0, limite + 1):
        resultado += i*i
    return resultado

print(sumaTodos(100))
print(sumaLosCuadrados(3))