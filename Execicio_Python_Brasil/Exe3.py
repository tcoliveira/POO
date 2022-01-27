class Retangulo():
    def __init__(self, Comprimento, Largura):
        self.Comprimento = Comprimento
        self.Largura = Largura

    def mudarComprimento(self):
        self.Comprimento = Comprimento

    def mudarLargura(self):
        self.Largura = Largura

    def retornaLados(self):
        return self.Largura

    def calculaArea(self):
        return self.Largura * self.Comprimento

Larg = int(input('Qual a largura: '))
Comp = int(input('Qual a Comprimento: '))
Ret = Retangulo(Comp,Larg)
print(Ret.calculaArea())



