#class Termometro():
    #def __init__(self, temperatura, unidadDeMedida):
        #self.temperatura = temperatura
        #self.unidadDeMedida = unidadDeMedida
        
class Termometro(): # simulamos un termometr0, creamos la clase termometro
    def __init__(self):  # hago la inicializacion, el constructor de mi termometro
        self.__temperatura = 0  # simulamos el atributo temperatura que trae el termometro
        self.__unidadDeMedida = 'c'  # simulamos el atributo unidad de medida que trae el termometro
    
    
    #def conversor(self):
        #if self.unidadDeMedida.lower() == 'c':
            #return (self.temperatura * 9/5) + 32
        #else:
            #return (self.temperatura - 32) * (5 / 9)
        
    def __conversor(self, temperatura, unidad):  # esta es la funcion conversor, que se encarga de convertirnos la medida
        if unidad.upper() == 'C':
            return "{} °F".format(temperatura * 9/5 + 32)
        elif unidad.upper() == 'F':
            return "{} °C".format((temperatura - 32) * 5 / 9)
        else:
            return "Unidad incorrecta"
        
    def __str__(self):  # modificamos la funcion impresion para que nos devuelva lo que queremos mostrar
        return "{}° {}".format(self.__temperatura,self.__unidadDeMedida)
    
    def unidadMedida(self, unidMed = None):  # aqui informamos la medida que vamos a querer utilizar en el termometro o la obtenemos
        if unidMed == None:
            return self.__unidadDeMedida
        else:
            if unidMed.upper() == 'F' or unidMed.upper == 'C':
                self.__unidadDeMedida = unidMed
                
    def temp(self, temperatura = None): # aqui informamos la temp que vamos a querer utilizar en el termometro o la obtenemos
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide(self, unidMed = None):  # esta es una funcion, publica, es lo que va a hacer el termometro, tiene un parametro que se
        if unidMed == None or unidMed == self.__unidadDeMedida:  # informa o no
            return self.__str__()
        else:
            if unidMed == 'C' or unidMed == 'F':
                return self.__conversor(self.__temperatura, self.__unidadDeMedida)
            else:
                return self.__str__
        
        
# c = Termometro()         
# c.conversor(0,'c')    
# t = Termometro()
# t.unidadMedida('F')
# t.temp(32)
# t.mide('c')
# t.mide('f')