import regraConversor

class RegraConversorMetro(regraConversor.RegraConversor):
    def __init__(self, quantidade, unidade):
        super().__init__(quantidade, unidade) 

    def calcular(self):
        milha = self.quantidade * 0.000621371
        polegada = self.quantidade * 39.3701
        pe = self.quantidade * 3.28084
        centimetro = self.quantidade * 100
        metro = self.quantidade
        quilometro = self.quantidade * 0.001
        
        print(
            self.quantidade, "metro(s) =", milha, "milha(s)\n",
            self.quantidade, "metro(s) =", polegada, "polegadas(s)\n",
            self.quantidade, "metro(s) =", pe, "pé(s)\n",
            self.quantidade, "metro(s) =", centimetro, "cm(s)\n",
            self.quantidade, "metro(s) =", metro, "m(s)\n",
            self.quantidade, "metro(s) =", quilometro, "km(s)\n",
        )
