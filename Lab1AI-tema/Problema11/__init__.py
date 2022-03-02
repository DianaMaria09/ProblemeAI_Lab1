'''Considerându-se o matrice cu n x m elemente binare (0 sau 1), 
să se înlocuiască cu 1 toate aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1.
'''

def inlocuire(n, m, matrice):
    '''
        n, m - nr intregi
        matrice - vector de elemente binare
        se returneaza matricea rezultata dupa inlocuire
    '''
    '''
        Complexitate generala: theta(n*m)
        Caz favorabil: theta(n*m)
        Caz nefavorabil: theta(n*m)
        Caz mediu: theta(n*m)
    '''
    for i in range(0, n-2):
        for j in range(0,m-2):
            ok = 1
            if (matrice[i][j] == 0 and matrice[i][j+1] == 0):
                if(matrice[i-1][j-1] !=1 or matrice[i-1][j] != 1 or matrice[i-1][j+1] != 1 or matrice[i-1][j+2] != 1):
                    ok = 0
                if(matrice[i+2][j-1] !=1 or matrice[i+2][j] != 1 or matrice[i+2][j+1] != 1 or matrice[i+2][j+2] != 1):
                    ok = 0
                if(matrice[i-1][j-1] !=1 or matrice[i][j-1] != 1 or matrice[i+1][j-1] != 1 or matrice[i+2][j-1] != 1):
                    ok = 0
                if(matrice[i-1][j+2] !=1 or matrice[i][j+2] != 1 or matrice[i+1][j+2] != 1 or matrice[i+1][j+2] != 1):
                    ok = 0
        if ok == 1:
            matrice[i][j] = 1
            matrice[i][j+1] = 1
            
    return matrice

def testPb11():
    assert (inlocuire(8, 10, [[1,1,1,1,0,0,1,1,0,1],[1,0,0,1,1,0,1,1,1,1],[1,0,0,1,1,1,1,1,1,1],[1,1,1,1,0,0,1,1,0,1],[1,0,0,1,1,0,1,1,0,0],[1,1,0,1,1,0,0,1,0,1],[1,1,1,0,1,0,1,0,0,1],[1,1,1,0,1,1,1,1,1,1]]) == [[1,1,1,1,0,0,1,1,0,1],[1,1,1,1,1,0,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,0,1],[1,1,1,1,1,1,1,1,0,0],[1,1,1,1,1,1,1,1,0,1],[1,1,1,0,1,1,1,0,0,1],[1,1,1,0,1,1,1,1,1,1]])
    #inlocuire(8, 10, [[1,1,1,1,0,0,1,1,0,1],[1,0,0,1,1,0,1,1,1,1],[1,0,0,1,1,1,1,1,1,1],[1,1,1,1,0,0,1,1,0,1],[1,0,0,1,1,0,1,1,1,1],[1,1,0,1,1,0,0,1,0,1],[1,1,1,0,1,0,1,0,0,1],[1,1,1,0,1,1,1,1,1,1]])
testPb11()