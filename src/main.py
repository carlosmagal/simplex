import numpy as np
from simplex import Simplex
#n == linhas
#m = restricoes
#m+1 total de colunas
#m+n+1 numero total de colunas com o tableu

def getInput():
  n, m = map(int, input().split())

  arrayC = np.array([input().strip().split()], float)
  arrayC = np.append(np.zeros(n), arrayC)
  arrayC = np.append(arrayC, [0])

  matrixInput = np.array([input().strip().split() for _ in range(n)], int)

  identity = np.identity(n)
  matrix = np.array(arrayC)

  for i in range(n):#tableau
    matrix = np.vstack([matrix, np.concatenate((identity[i],matrixInput[i]))])

  return n, m, matrix

# n, m, matrix = getInput()

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


teste = np.array([
  [0. ,0. , 0. ,2. ,4. ,8. , 0.],
  [1. ,0. , 0. ,1. ,0. ,0. , 1.],
  [0. ,1. , 0. ,0. ,1. ,0. , 1.],
  [0. ,0. , 1. ,0. ,0. ,1. , 1.],
])#ótimo 14
simplex = Simplex(3, 3, teste)

teste = np.array([
  [0. ,0. , 0. ,0. , -3., -4. , 5., -5., 0.],
  [1. ,0. , 0. ,0. , 1., 1. , 0., 0., 5.],
  [0. ,1. , 0. ,0. , -1., 0. , -5. , 5., -10.],
  [0. ,0. , 1. ,0. , 2., 1. , 1., -1., 10.],
  [0. ,0. , 0. ,1. , -2., -1. , -1., 1., 10.],
])#ótimo 50
simplex = Simplex(4, 4, teste)

teste = np.array([
  [0. ,0. , 0. ,0. , 1., 1. , 1., 0.],
  [1. ,0. , 0. ,0. , 1., 0. , 0., -1.],
  [0. ,1. , 0. ,0. , 0., 1. , 0. , -1.],
  [0. ,0. , 1. ,0. , 0., 0. , 1., -1.],
  [0. ,0. , 0. ,1. , 1., 1. , 1., -1.],
])#inviavel 
simplex = Simplex(4, 3, teste)


simplex.run()