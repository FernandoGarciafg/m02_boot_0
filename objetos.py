import turtle  # importamos la tortuga

tortuguita = turtle.Turtle()  # creamos un objeto del modulo turtle de tipo turtle, los objetos van siempre con mayuscula, el nombre
                              # del tipo de objeto va siempre con mayuscula, en el fondo son funciones de primer nivel capaces de
                              # llamarse e invocarse y crear copias de si mismas

# la ventaja de los objetos es que por ej ahora podriamos crearnos otra tortuguita
otraTortuguita = turtle.Turtle()

tortuguita.fd(50)  # le damos una instrucciona nuestra tortuguita

# le damos instrucciones a la otra tortuguita
otraTortuguita.color('red')
otraTortuguita.left(90)
otraTortuguita.fd(50)

# tenemos el codigo turtle encapsulado, que esta en el modulo turtle, en este objeto de tipo turtle hay un codigo que es capaz de
# ejecutar ciertas funciones como avanzar y girar pero yo puedo crearme tantas instancias de este objeto como quiera, son funciones
# de primer nivel capaces de invocarse a si mismas y crear copias de si mismas
# esto sirve por ej para poder crear 2 jugadores en un juego, ambos van a tener la mismas funcionalidades pero no los mismos
# atributos, podemos tener objetos que teniendo el mismo codigo tengan comportamientos distintos y sus atributos-propiedades sean
# distintas




















