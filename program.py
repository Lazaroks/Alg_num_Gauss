import numpy as np

def napraw(wynik, i):
    n=i
    for j in range(i, len(wynik)):
        if wynik[j][i]!=0:
            n=j
    if n==i: 
        print("Macierz nie jest policzalna!")
        return False
    else: 
        wynik[[i, n]]=wynik[[n, i]]
        return True

def wypisz_krok(wynik, licz):
    print(licz)
    print(wynik)
    print("\n")

def wyznacz(wynik):
    det=1
    for i in range(len(wynik)):
        if wynik[i][i]==0:
            if not napraw(wynik, i): return
        for j in range(i+1, len(wynik)):
            licz=wynik[j][i]/wynik[i][i]
            for z in range(i, len(wynik)):
                wynik[j][z]=wynik[j][z]-(licz*wynik[i][z])
            wypisz_krok(wynik,licz)
        det=det*wynik[i][i]
    print("Wyznacznik macierzy det(A) = " + str(det))    
                
    
wynik=np.array([[1,3,0,-1],[1,2,3,3],[3,1,1,1],[3,2,0,3]], dtype=float)
wynik2=np.array([[1,-2,1,1],[2,-4,-1,1],[-1,2,2,-1],[1,-2,-1,-1]], dtype=float)
wyznacz(wynik2)