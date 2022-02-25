'''
Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii, 
să se identifice indexul liniei care conține cele mai multe elemente de 1.
De ex. în matricea
[[0,0,0,1,1],
[0,1,1,1,1],
[0,0,1,1,1]]
a doua linie conține cele mai multe elemente 1.
'''

def elementeLinie(n, m, matrice):
    '''
        n - nr de linii
        m - nr de coloane
        matrice - lista de liste de 0 si 1
        se returneaza nr liniei cu cei mai multi 1
    '''
    '''
        Complexitate: theta(n^2*m) - pentru ca se parcurg liniile si coloanele, iar apoi inca o daca un sir de dimensiunea n
        Caz favorabil: theta(n^2*m)
        Caz nefavorabil: theta(n^2*m)
        Caz mediu: theta(n^2*m)
    '''
    frecventa = [0] * n
    for i in range(0, n):
        for j in range (0, m):
            if (matrice[i][j] == 1):
                frecventa[i] += 1
    maxim = 0
    for i in range(0, n):
        if frecventa[i] > maxim:
            maxim = frecventa[i]
            linia = i
    print(linia + 1)
    return linia + 1

def testPb10():
    assert elementeLinie(3, 5, [[0,0,0,1,1],[0,1,1,1,1],[0,0,1,1,1]]) == 2
    assert elementeLinie(3, 5, [[1,1,1,1,1],[0,1,1,1,1],[0,0,1,1,1]]) == 1
    assert elementeLinie(3, 5, [[0,0,0,1,1],[0,1,1,1,1],[0,1,1,1,1]]) == 2
    assert elementeLinie(2, 2, [[0,1],[1,1]]) == 2

testPb10()