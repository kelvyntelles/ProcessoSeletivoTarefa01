import regraConversor

class RegraConversorMilha(regraConversor.RegraConversor):
    def __init__(self, quantidade, unidade):
        super().__init__(quantidade, unidade) 

    def calcular(self):
        milha = self.quantidade
        polegada = self.quantidade * 63360
        pe = self.quantidade * 5280
        centimetro = self.quantidade * 160934
        metro = self.quantidade * 1609.34
        quilometro = self.quantidade * 128.748
        
        print(
            self.quantidade, "milha(s) =", milha, "milha(s)\n",
            self.quantidade, "milha(s) =", polegada, "polegadas(s)\n",
            self.quantidade, "milha(s) =", pe, "pé(s)\n",
            self.quantidade, "milha(s) =", centimetro, "cm(s)\n",
            self.quantidade, "milha(s) =", metro, "m(s)\n",
            self.quantidade, "milha(s) =", quilometro, "km(s)\n",
        )
