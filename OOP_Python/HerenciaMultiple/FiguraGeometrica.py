class FiguraGeometrica:
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self.ancho = 0
            print(f"Valor erroneo ancho: {ancho}")

        if self._validar_valor(alto) :
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erroneo alto : {alto}")
    
    @property #getter
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erroneo ancho: {ancho} , se mantiene el valor previo a esta modificacion fallida")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._ancho = ancho
        else:
            print(f"Valor erroneo ancho: {alto} , se mantiene el valor previo a esta modificacion fallida")

    
    def __str__(self):
        return f"class FiguraGeometrica [ancho: {self._ancho}, alto: {self._alto}] "

    def _validar_valor(self, valor):
        """ es un numero mayor a 0 y menor a 10?"""
        return True  if(0 < valor < 10)   else False

        
    