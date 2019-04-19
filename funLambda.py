from funPrimerNivel import sumaTodos 

doble = lambda x: x * 2
#sumaTodos(3, doble)

triple = lambda x: x**3

#print(sumaTodos(100, lambda x: x**3))
print(sumaTodos(100, doble))
#print(sumaTodos(100, lambda x: x**3))
print(sumaTodos(100, triple))
