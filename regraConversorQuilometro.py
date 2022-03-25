import regraConversor

class RegraConversorQuilometro(regraConversor.RegraConversor):
    def __init__(self, quantidade, unidade):
        super().__init__(quantidade, unidade) 

    def calcular(self):
        milha = self.quantidade * 0.621371
        polegada = self.quantidade * 39370.1
        pe = self.quantidade * 3280,84
        centimetro = self.quantidade * 100000
        metro = self.quantidade * 1000
        quilometro = self.quantidade
        
        print(
            self.quantidade, "km(s) =", milha, "milha(s)\n",
            self.quantidade, "km(s) =", polegada, "polegadas(s)\n",
            self.quantidade, "km(s) =", pe, "pé(s)\n",
            self.quantidade, "km(s) =", centimetro, "cm(s)\n",
            self.quantidade, "km(s) =", metro, "m(s)\n",
            self.quantidade, "km(s) =", quilometro, "km(s)\n",
        )
