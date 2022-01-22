class Quadrado():
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def mudarLado(self):
        self.tamanho = tamanho

    def retornaLado(self):
        return self.tamanho
    def calculaArea(self):
        return self.tamanho * 2

b = Quadrado(10)
print(b.retornaLado())
