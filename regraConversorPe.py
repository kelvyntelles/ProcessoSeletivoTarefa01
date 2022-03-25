import regraConversor

class RegraConversorPe(regraConversor.RegraConversor):
    def __init__(self, quantidade, unidade):
        super().__init__(quantidade, unidade) 

    def calcular(self):
        milha = self.quantidade * 0.000189394
        polegada = self.quantidade * 12
        pe = self.quantidade
        centimetro = self.quantidade * 30.48
        metro = self.quantidade * 0.3048
        quilometro = self.quantidade * 0.0003048
        
        print(
            self.quantidade, "pé(s) =", milha, "milha(s)\n",
            self.quantidade, "pé(s) =", polegada, "polegadas(s)\n",
            self.quantidade, "pé(s) =", pe, "pé(s)\n",
            self.quantidade, "pé(s) =", centimetro, "cm(s)\n",
            self.quantidade, "pé(s) =", metro, "m(s)\n",
            self.quantidade, "pé(s) =", quilometro, "km(s)\n",
        )
