import numpy as np
from simplex import Simplex, auxiliar
#n == linhas
#m = restricoes
#m+1 total de colunas
#m+n+1 numero total de colunas com o tableu
# o c da auxiliar vai ter M 0's e N -1's

def getInput():
  n, m = map(int, input().split())

  arrayC = np.array([input().strip().split()], float)#pegando o c normal
  arrayC = np.append(np.zeros(n), arrayC)#colocando n zeros antes do c
  arrayC = np.append(arrayC, [0])#colocando um 0 no final do c

  matrixInput = np.array([input().strip().split() for _ in range(n)], int)

  matrixAuxiliar = auxiliar(n, m, matrixInput)

  identity = np.identity(n)
  matrix = np.array(arrayC)

  for i in range(n):#tableau
    matrix = np.vstack([matrix, np.concatenate((identity[i],matrixInput[i]))])

  return n, m, matrix, matrixAuxiliar

n, m, matrix, matrixAuxiliar = getInput()
# simplex = Simplex(n, m, matrix, matrixAuxiliar)

simplex = Simplex(n, m+n, matrixAuxiliar,matrix)


# teste = np.array([
#   [0. ,0. , 0. ,2. ,4. ,8. , 0.],
#   [1. ,0. , 0. ,1. ,0. ,0. , 7.],
#   [0. ,1. , 0. ,2. ,1. ,0. , 4.],
#   [0. ,0. , 1. ,1. ,0. ,1. , 9.],
# ])
# simplex = Simplex(3, 3, teste)

# teste = np.array([
#   [0. ,0. ,0. ,3. ,-7. , 0. ,-8.],
#   [1. ,0. ,1. ,2. ,-2. , 0. ,2. ],
#   [0. ,1. ,0. ,1. ,3. , 1. ,5. ],
# ]) 
# simplex = Simplex(2, 4, teste)


# teste = np.array([
#   [0. ,0. , 0. ,2. ,4. ,8. , 0.],
#   [1. ,0. , 0. ,1. ,0. ,0. , 1.],
#   [0. ,1. , 0. ,0. ,1. ,0. , 1.],
#   [0. ,0. , 1. ,0. ,0. ,1. , 1.],
# ])#ótimo 14
# simplex = Simplex(3, 3, teste)

# teste = np.array([
#   [0. ,0. , 0. ,0. , -3., -4. , 5., -5., 0.],
#   [1. ,0. , 0. ,0. , 1., 1. , 0., 0., 5.],
#   [0. ,1. , 0. ,0. , -1., 0. , -5. , 5., -10.],
#   [0. ,0. , 1. ,0. , 2., 1. , 1., -1., 10.],
#   [0. ,0. , 0. ,1. , -2., -1. , -1., 1., 10.],
# ])#ótimo 50
# simplex = Simplex(4, 4, teste)

# teste = np.array([
#   [0. ,0. , 0. ,0. , 1., 1. , 1., 0.],
#   [1. ,0. , 0. ,0. , 1., 0. , 0., -1.],
#   [0. ,1. , 0. ,0. , 0., 1. , 0. , -1.],
#   [0. ,0. , 1. ,0. , 0., 0. , 1., -1.],
#   [0. ,0. , 0. ,1. , 1., 1. , 1., -1.],
# ])#inviavel 
# simplex = Simplex(4, 3, teste)


# teste = np.array([
#   [0. ,0. , 0. ,0. , 1., 1. , 1., 0.],
#   [1. ,0. , 0. ,0. , 1., 0. , 0., -1.],
#   [0. ,1. , 0. ,0. , 0., 1. , 0. , -1.],
#   [0. ,0. , 1. ,0. , 0., 0. , 1., -1.],
#   [0. ,0. , 0. ,1. , 1., 1. , 1., -1.],
# ])#inviavel 
# simplex = Simplex(8, 6, teste)

simplex.runAuxiliar()


