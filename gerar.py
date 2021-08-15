from itertools import count
import random as rand

class Gerador:

    def __init__(self):
        pass

    def aleatorio(configuracoes_loteria):

        aposta = []
        del aposta[:]

        id_dezena = []
        del id_dezena[:]

        id_aposta = []
        del id_aposta[:]

        for n in range(configuracoes_loteria[1]):

            quadrante = rand.randint(0,3)
            conjunto = rand.randint(0,4)
            dezena = rand.randint(0,4)

            if configuracoes_loteria[0] == 1:
                if quadrante >= 2:
                    conjunto = 0

            id_dezena = [quadrante,conjunto,dezena]

            if id_aposta.count(id_dezena):
                id_dezena = []
                del id_dezena[:]

                quadrante = rand.randint(0,3)
                conjunto = rand.randint(0,4)
                dezena = rand.randint(0,4)
                id_dezena = [quadrante,conjunto,dezena]
                id_aposta.append(id_dezena)
            else:
                id_aposta.append(id_dezena)
    
        return id_aposta


    # print(aleatorio(x,configuracoes_loteria))









