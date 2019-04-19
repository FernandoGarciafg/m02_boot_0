def sumaTodos(limite):
    resultado = 0
    for i in range(0, limite + 1):
        resultado = resultado + i
    
    return resultado

print(sumaTodos(10))