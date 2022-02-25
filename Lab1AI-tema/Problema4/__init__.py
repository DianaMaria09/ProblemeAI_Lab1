'''
Să se determine cuvintele unui text care apar exact o singură dată în acel text. 
De ex. cuvintele care apar o singură dată în "ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.
'''

def cuvinteUnice(text):
    cuvinte = text.split()
    print(cuvinte)
    unice = ""
    for x in range(0, len(cuvinte)-1):
        ok = 1
        for y in range (x+1, len(cuvinte)):
            if cuvinte[x] == cuvinte[y]:
                ok = 0
                print("am gasit: ")
                print(cuvinte[x])
                print(ok)
        if ok == 1:
            unice = unice + cuvinte[x] + " "
    print(unice)
    print("la final")
    return unice

def testPb4():
    assert cuvinteUnice("Ana are mere pere mere si pere") == "Ana are si"
    
testPb4()