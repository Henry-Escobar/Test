class Calculadora:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def sumar(self):
        return self.numero_1 + self.numero_2

    def restar(self):
        return self.numero_1 - self.numero_2

    def multiplicar(self):
        return self.numero_1 * self.numero_2

    def dividir(self):
        if self.numero_2 != 0:
            return self.numero_1 / self.numero_2
            # return self.numero_1 // self.numero_2
        else:
            return "No se puede realizar la division"


calculadorita = Calculadora(10, 5)
print(calculadorita.restar())
print(calculadorita.multiplicar())
print(calculadorita.sumar())
print(calculadorita.dividir())
