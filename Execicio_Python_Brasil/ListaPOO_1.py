class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def trocaCor(self):
        self.cor = cor

    def mostraCor(self):
        return self.cor

b = Bola('Azul', 10, 'couro')
print(b.mostraCor())