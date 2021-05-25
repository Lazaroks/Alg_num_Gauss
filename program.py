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
    licznik_podmianek = 0
    for i in range(len(wynik)):
        if wynik[i][i]==0:
            if not napraw(wynik, i): return
            else: licznik_podmianek += 1
        for j in range(i+1, len(wynik)):
            licz=wynik[j][i]/wynik[i][i]
            for z in range(i, len(wynik)):
                wynik[j][z]=wynik[j][z]-(licz*wynik[i][z])
            # print("{}\n{}\n".format(licz, wynik))
        det=det*wynik[i][i]
    det = det * ( (-1)**licznik_podmianek ) 
    print("Wyznacznik macierzy det(A) = " + str(det))    
                
def mapa(x, y):
    if x == 't':
        return y
    else:
        return x


# wynik=np.array([[1,3,0,-1],[1,2,3,3],[3,1,1,1],[3,2,0,3]], dtype=float)
# wynik2=np.array([[1,-2,1,1],[2,-4,-1,1],[-1,2,2,-1],[1,-2,-1,-1]], dtype=float)

try:
    with open("dane.txt") as f:
        lines = f.readlines()
        t_flag = 0
        for line in lines:
            if 't' in line:
                t_flag = 1
        
        if t_flag == 0:
            matrix = []
            for line in lines:
                matrix.append(line.split(" "))
            macierz = np.array(matrix, dtype=float)
            wyznacz(macierz)
        else:
            # matrices = []
            zakres = range(-5, 5)
            for i in zakres:
                matrix = []
                for line in lines:
                    matrix.append( list( map( lambda x: mapa(x, i), line.split(" ") ) ) )
                macierz = np.array(matrix, dtype=float)
                print("Dla parametru t = ",i)
                wyznacz(macierz)
                print("\n")


except FileNotFoundError:
    print("File not found")
