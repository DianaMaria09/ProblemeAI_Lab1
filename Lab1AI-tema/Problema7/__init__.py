'''
Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n). 
De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.
'''

def kMaxim(sir,k):
    '''
        sir - sirul de numere
        k - nr intreg
        se returneaza al k-lea maxim din sir
        se arunca exceptie dc k>n, unde n este dimensiunea sirului
    '''
    '''
        Complexitate: O(nlogn)- complexiatea sortarii
        Caz favorabil: O(n)
        Caz nefavorabil: O(nlogn)
        Caz mediu: O(nlogn)
    '''
    sir = list(dict.fromkeys(sir))
    sir.sort(reverse = True)
    if k > len(sir):
        raise ValueError("k trebuie sa fie mai mic decat dimensiunea sirului")
    else: 
        return sir[k-1]

def testPb7():
    assert kMaxim([7,4,6,3,9,1], 2) == 7
    assert kMaxim([7,4,6,3,9,1], 3) == 6
    assert kMaxim([7,4,6,3,9,1], 1) == 9
    assert kMaxim([2,2,3,4,5,4,1,1], 2) == 4
    try:
        kMaxim([2,2,3,4,5,4,1,1], 13)
    except ValueError:
        print("k trebuie sa fie mai mic decat dimensiunea sirului")
        
testPb7()