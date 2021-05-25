import numpy as np


def napraw(wynik, i):
    n=i
    for j in range(i, len(wynik)):
        if wynik[j][i]!=0:
            n=j
            break
    if n==i: 
        print("Wyznacznik równy 0")
        return False
    else: 
        wynik[[i, n]]=wynik[[n, i]]
        return True

def wyznacz(wynik):
    det=1
    for i in range(len(wynik)):
        if wynik[i][i]==0:
            if not napraw(wynik, i): return
        for j in range(i+1, len(wynik)):
            licz=wynik[j][i]/wynik[i][i]
            for z in range(i, len(wynik)):
                wynik[j][z]=wynik[j][z]-(licz*wynik[i][z])
            print("{}\n{}\n".format(licz, wynik))
        det=det*wynik[i][i]
    print("Wyznacznik macierzy det(A) = {}".format(det))    
                
    
wynik=np.array([[1,3,0,-1],[1,2,0,3],[3,1,1,1],[0,2,0,3]], dtype=float)
wynik2=np.array([[1,-2,1,1],[2,-4,-1,1],[-1,2,2,-1],[1,-2,-1,-1]], dtype=float)
wyznacz(wynik)

try:
    with open("dane.txt") as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            matrix.append(line.split(" "))
        wynik2 = np.array(matrix, dtype=float)
        wyznacz(wynik2)
except FileNotFoundError:
    print("File not found")