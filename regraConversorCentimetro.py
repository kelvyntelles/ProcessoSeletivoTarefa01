import regraConversor

class RegraConversorCentimetro(regraConversor.RegraConversor):
    def __init__(self, quantidade, unidade):
        super().__init__(quantidade, unidade) 

    def calcular(self):
        milha = self.quantidade * 6.2137
        polegada = self.quantidade * 0.3937008
        pe = self.quantidade * 0.0328084
        centimetro = self.quantidade
        metro = self.quantidade * 0.01
        quilometro = self.quantidade * 1
        
        print(
            self.quantidade, "cm(s) =", milha, "milha(s)\n",
            self.quantidade, "cm(s) =", polegada, "polegadas(s)\n",
            self.quantidade, "cm(s) =", pe, "pé(s)\n",
            self.quantidade, "cm(s) =", centimetro, "cm(s)\n",
            self.quantidade, "cm(s) =", metro, "m(s)\n",
            self.quantidade, "cm(s) =", quilometro, "km(s)\n",
        )
