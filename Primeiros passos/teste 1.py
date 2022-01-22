class Caneca:
    logo = ''
    cor = ''
    nome = ''

    def beber(self):
        print('Bebendo caneca', self.nome)
caneca1 = Caneca()
caneca1.logo = 'Teste'
caneca1.nome = 'canecanome'


print(caneca1.logo)

caneca1.beber()