class Construtor:

    def __init__(self):
        pass

    def aposta():
        pass

    def geral():
        pass

    def conjunto():
        pass

    


x=[
        [
            [1,2,3,4,5],
            [11,12,13,14,15],
            [21,22,23,24,25]
        ],
        [
            [6,7,8,9,10],
            [16,17,18,19,20],
            [26,27,28,29,30]
        ],
        [
            [31,32,33,34,35],
            [41,42,43,44,45],
            [51,52,53,54,55]
        ],
        [
            [36,37,38,39,40],
            [46,47,48,49,50],
            [56,57,58,59,60]
        ]
    ]

for a in range(len(x)):
    # print('a:',a)
    for b in range(len(x[a])):
        # print('b:',b)
        for c in range(len(x[a][b])):
            print(x[a][b][c])


