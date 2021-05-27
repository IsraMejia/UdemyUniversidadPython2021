class Aritmetica:
    """Esta clase tiene codigo util para hacer operaciones aritmeticas """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB

    

print("\n\tEn este programa se crea la clase Aritmetica y se pone a prueba")

aritmetica1 = Aritmetica(4, 3)
print(f'La suma es : {aritmetica1.sumar()}')
print(f'La resta es : {aritmetica1.restar()}')
print(f'La multiplicacion es : {aritmetica1.multiplicar()}')
print(f'La division es : {aritmetica1.dividir():.2f}') # con el :.2f solo se muestran dos numeros flotantes (decimales xd)
        
