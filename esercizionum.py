import numpy as np

#genero un array randomico 6x6
array=np.random.randint(1,100,(6,6))
print(array)
#separo le righe 4x4
sottomatrice=array[1:5,1:5]
print("sotto matrice 4x4",sottomatrice)
#inverto l'ordine delle righe
matrice_invertita=np.transpose(sottomatrice)
print("matrice invertita",matrice_invertita)
#estraggo la diagonale dell array
diagonale=np.diagonal(matrice_invertita)
print("diagoneale",diagonale)
#sostisuisco gli elementi multipli di 3 con -1
matrice_invertita[matrice_invertita % 3 == 0] = -1
print(matrice_invertita)





