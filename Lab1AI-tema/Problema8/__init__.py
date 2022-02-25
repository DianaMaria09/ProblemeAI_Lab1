'''
Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n. 
De ex. dacă n = 4, numerele sunt: 1, 10, 11, 100.
'''
def schimbareBaza(nr):
    putere = 1
    nrInBaza2 = 0
    while nr > 0:
        cifra = nr % 2
        nrInBaza2 = nrInBaza2 + putere * cifra
        putere = 10 * putere
        nr = nr / 2
    print(nrInBaza2)
    return nrInBaza2

def testPb8():
    schimbareBaza(10)
    
testPb8()