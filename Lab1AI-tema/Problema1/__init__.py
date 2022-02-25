'''
Sa se determine ultimul (din punct de vedere alfabetic) cuvant 
care poate aparea intr-un text care conține mai multe cuvinte separate prin "" (spatiu). 
De ex. ultimul (dpdv alfabetic) cuvânt din "Ana are mere rosii si galbene" este cuvântul "si".
'''
def ultimCuvant(propozitie):
    '''
        Complexitate: theta(n)- se parcurge liniar sirul de cuvinte
        Caz favorabil: theta(n)
        Caz nefavorabil: theta(n)
        Caz mediu: theta(n)
        In toate cazurile se parcurge sirul pana la capat, ceea ce inseamna ca si cazul nefavorabil
            si cel favorabil au complexitate theta(n), ceea ce conduce la o complexitate medie de theta(n).
            n - dimensiunea
    '''
    #imparte propozitia in cuvinte si apoi returneaza ultimul cuvant alfabetic (cel cu codul ascii cel mai mare)
    cuvinte = propozitie.split()
    maxim = ""
    for c in cuvinte: 
        #print(c)
        if c > maxim:
            maxim = c
    #print(maxim)
    return maxim

def testPb1(): 
    assert ultimCuvant("Ana are mere") == "mere"
    assert ultimCuvant("Ana are mere si portocale") == "si"
    assert ultimCuvant("Ana are mere si sirop") == "sirop"
    assert ultimCuvant("Ana are mere si zmeura") == "zmeura"

testPb1()