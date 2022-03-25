import regraConversor

class RegraConversorPolegada(regraConversor.RegraConversor):
    def __init__(self, quantidade, unidade):
        super().__init__(quantidade, unidade)
    
    def calcular(self):
        milha = self.quantidade * 1.5783
        polegada = self.quantidade
        pe = self.quantidade * 0.0833333
        centimetro = self.quantidade * 2.54
        metro = self.quantidade * 0.0254
        quilometro = self.quantidade * 2.54
        
        print(
            self.quantidade, "polegada(s) =", milha, "milha(s)\n",
            self.quantidade, "polegada(s) =", polegada, "polegadas(s)\n",
            self.quantidade, "polegada(s) =", pe, "pé(s)\n",
            self.quantidade, "polegada(s) =", centimetro, "cm(s)\n",
            self.quantidade, "polegada(s) =", metro, "m(s)\n",
            self.quantidade, "polegada(s) =", quilometro, "km(s)\n",
        )

