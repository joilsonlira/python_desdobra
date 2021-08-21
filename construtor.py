from gerar import *


class Construtor:
    x=[
        [
            [1,2,3,4,5],
            [11,12,13,14,15],
            [21,22,23,24,25],
            [31,32,33,34,35],
            [41,42,43,44,45]
                
        ],
        [
            [6,7,8,9,10],
            [16,17,18,19,20],
            [26,27,28,29,30],
            [36,37,38,39,40],
            [46,47,48,49,50]
        ],
        [
            [51,52,53,54,55],
            [61,62,63,64,65],
            [71,72,73,74,75],
            [81,82,83,84,85],
            [91,92,93,94,95]
        ],
        [
            [56,57,58,59,60],
            [66,67,68,69,70],
            [76,77,78,79,80],
            [86,87,88,89,90],
            [96,97,98,99,100]
        ]
    ]
    configuracoes_loteria = [1,6]

    id_aposta = Gerador.aleatorio(configuracoes_loteria)
    print(id_aposta)

    def __init__(self):
        pass

    
    def aposta(id_aposta,x):
        
        aposta=[]
        del aposta[:]

        for a in range(len(id_aposta)):
            
            id_dezena = [id_aposta[a][0],id_aposta[a][1],id_aposta[a][2]]
            aposta.append(x[id_dezena[0]][id_dezena[1]][id_dezena[2]])

        return sorted(aposta)
    

    def dezena():
        pass

    print(aposta(id_aposta,x))




