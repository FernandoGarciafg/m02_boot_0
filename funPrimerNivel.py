def normal(x):
    return x

def cuadrado(y):
    return y * y

def cubo(x):
    return x**3
    

def sumaTodos(limite, f):
    resultado = 0
    for i in range(limite + 1):
        resultado += f(i)
    return resultado

if __name__ == '__main__':
    print(sumaTodos(100,normal))
    print(sumaTodos(3,cuadrado))