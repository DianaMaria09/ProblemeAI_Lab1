'''
    Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate din coordonatele a 2 căsuțe 
    din matrice ((p,q) și (r,s)), 
    să se calculeze suma elementelor din sub-matricile identificate de fieare pereche.
    De ex, pt matricea
    [[0, 2, 5, 4, 1],
     [4, 8, 2, 3, 7],
     [6, 3, 4, 6, 2],
     [7, 3, 1, 8, 3],
     [1, 5, 7, 9, 4]]
și lista de perechi ((1, 1) și (3, 3)), ((2, 2) și (4, 4)), 
suma elementelor din prima sub-matrice este 38, iar suma elementelor din a 2-a sub-matrice este 44.
'''
def sumaSubmatrici(p, q, r, s, matrice):
    '''
        p,q,r,s - nr intregi
        matrice - matrice de 0 si 1
        se returneaza suma elementelor din submatrice
    '''
    '''
        Complexitate: theta(n*m)- se parcurge submatricea
        Caz favorabil: theta(n*m)
        Caz nefavorabil: theta(n*m)
        Caz mediu: theta(n*m)
    '''
    suma = 0
    for i in range(p, r + 1):
        for j in range (q, s + 1):
            suma = suma + matrice [i][j]
    return suma

def testPb9():
    assert sumaSubmatrici(1, 1, 3, 3, [[0, 2, 5, 4, 1],[4, 8, 2, 3, 7],[6, 3, 4, 6, 2],[7, 3, 1, 8, 3],[1, 5, 7, 9, 4]]) == 38
    assert sumaSubmatrici(2, 2, 4, 4, [[0, 2, 5, 4, 1],[4, 8, 2, 3, 7],[6, 3, 4, 6, 2],[7, 3, 1, 8, 3],[1, 5, 7, 9, 4]]) == 44
    assert sumaSubmatrici(1, 1, 2, 2, [[0, 2, 5, 4, 1],[4, 8, 2, 3, 7],[6, 3, 4, 6, 2],[7, 3, 1, 8, 3],[1, 5, 7, 9, 4]]) == 17
    assert sumaSubmatrici(2, 2, 3, 3, [[0, 2, 5, 4, 1],[4, 8, 2, 3, 7],[6, 3, 4, 6, 2],[7, 3, 1, 8, 3],[1, 5, 7, 9, 4]]) == 19

testPb9()