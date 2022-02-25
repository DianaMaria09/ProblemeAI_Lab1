'''
Să se determine produsul scalar a doi vectori rari care conțin numere reale. 
Un vector este rar atunci când conține multe elemente nule. 
Vectorii pot avea oricâte dimensiuni. 
De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.
'''

def produsScalar(v1,v2):
    '''
        v1, v2 - vectori scalari (de numere reale)
        produs - produsul scalar returnat
    '''
    '''
        Complexitate: theta(n)- se parcurg liniar vectorii in paralel (deodata)
        Caz favorabil: theta(n)
        Caz nefavorabil: theta(n)
        Caz mediu: theta(n)
        In toate cazurile se parcurge sirul pana la capat, ceea ce inseamna ca si cazul nefavorabil
            si cel favorabil au complexitate theta(n), ceea ce conduce la o complexitate medie de theta(n).
            n - dimensiunea
    '''
    #v1 si v2 au aceeasi dimensiune
    produs = 0
    i=0
    #calculam produsul scalar al celor doi vectori, dupa formula  
    while i < len(v1):
        produs = produs + v1[i] * v2[i]
        i+=1
    #print(produs)
    return produs

def testPb3():
    assert produsScalar([1,1], [2,2]) == 4
    assert produsScalar([1,1,2.1], [2,2,3.0]) == 10.3
    assert produsScalar([0,1,9,0], [2,0,0,3]) == 0
    assert produsScalar([1,0,2,0,3], [1,2,0,3,1]) == 4
    
testPb3()