import regraConversorMilha
import regraConversorPolegada
import regraConversorPe
import regraConversorCentimetro
import regraConversorMetro
import regraConversorQuilometro

opcoes = ["0 - Milha", "1 - Polegada", "2 - Pé", "3 - Centímetro", "4 - Metro", "5 - Quilômetro"]

quantidade = int(input("Informe a quantidade: "))
print("opções", opcoes)
unidade = int(input("informe a opção desejada: "))
if unidade < 0 or unidade >= len(opcoes):
    unidade = int(input("informe a opção desejada: "))
    while unidade < 0 or unidade >= len(opcoes):
        unidade = int(input("informe a opção desejada: "))
    
if unidade == 0:
    dados = regraConversorMilha.RegraConversorMilha(quantidade, unidade)
    dados.calcular()
elif unidade == 1:
    dados = regraConversorPolegada.RegraConversorPolegada(quantidade, unidade)
    dados.calcular()
elif unidade == 2:
    dados = regraConversorPe.RegraConversorPe(quantidade, unidade)
    dados.calcular()
elif unidade == 3:
    dados = regraConversorCentimetro.RegraConversorCentimetro(quantidade, unidade)
    dados.calcular()
elif unidade == 4:
    dados = regraConversorMetro.RegraConversorMetro(quantidade, unidade)
    dados.calcular()
elif unidade == 5:
    dados = regraConversorQuilometro.RegraConversorQuilometro(quantidade, unidade)
    dados.calcular()
    
