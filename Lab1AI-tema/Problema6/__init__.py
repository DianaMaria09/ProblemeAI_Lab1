'''
Pentru un șir cu n numere întregi care conține și duplicate, 
să se determine elementul majoritar (care apare de mai mult de n / 2 ori). 
De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].
'''

def elementMajoritar(sir):
    '''
        sir - sirul de numere initial
        fr - sirul frecventelor (de cate ori apare fiecare nr), initializat cu 0
    '''
    '''
        Complexitate: O(n^2)- se parcurge de doua ori sirul de numere
        Caz favorabil: theta(n) - nu exista un element majoritar
        Caz nefavorabil: theta(n^2) - trebuie parcurs de doua ori sirul
        Caz mediu: O(n^2)
        
        Complexitatea dpdv al spatiului - consuma memorie pt sirul cu frecventele
    '''
    fr = [0] * 100
    #mai intai parcurgem sirul si calculam frecventele
    for x in sir:
        fr[x] = fr[x] + 1
    #print(max(fr))
    maxim = max(fr)
    #daca avem un element majoritar, il aflam
    if maxim >= len(sir)/2:
        for x in sir:
            if fr[x] == maxim:
                el = x
                #print(el)
        return el
    else:
        #daca nu, returnam un nr random si afisam un mesaj
        print("Nu exista un element majoritar")
        return -10

def testPb6():
    assert elementMajoritar([2,8,7,2,2,5,2,3,1,2,2]) == 2
    assert elementMajoritar([2,8,7,7,7,5,2,3,1,7,2]) == -10
    assert elementMajoritar([2,3,7,2,3,3,3,3,1,3,2]) == 3
    assert elementMajoritar([2,0,0,0,0,0,5,2,3,0,2,2]) == 0
    
testPb6()