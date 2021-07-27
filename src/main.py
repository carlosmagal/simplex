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

  return n, m, matrix, matrixAuxiliar, arrayC

n, m, matrix, matrixAuxiliar, arrayC = getInput()

simplex1 = Simplex(n, m+n, matrixAuxiliar, matrix)# simplex fase 1, monta a auxiliar

#######################################
def pivotingAuxiliar(matrix, n, m, column):
  if(matrix[0][column] == 0): return matrix

  for i in range(1, n+1):
    if(matrix[i][column] == 1):#pegando index da linha do pivo
      multiplier = -1 * matrix[0][column]
      for j in range(n+m+1):
        matrix[0][j] = matrix[0][j] + (multiplier*matrix[i][j])
        
  
  return matrix
##################################


# simplex.runAuxiliar()
if(simplex1.runAuxiliar()):
  print('tem zero no bagui')
	# pegar a auxiliar, retirar a matriz que foi colocada no meio(retirar a partir da m, n vezes)
	# trocar a linha c pela original
	# pivotear a primeira linha, para ficar 0 em cima das bases

  print(matrixAuxiliar)

  for i in range(m+n, n+n+m):
    print(i)
    matrixAuxiliar = np.delete(matrixAuxiliar, n+m, 1)

  print(matrixAuxiliar)

  matrixAuxiliar[0] = arrayC # talvez vai ser necessario pegar os n primeiros numeros da matriz auxiliar
  print(matrixAuxiliar)

  #BO
  #checar, a partir da linha n, quais colunas devem ser pivoteadas, pular a ultima 
	

  #pego a matriz a partir da linha n, e vejo a coluna que tem um '1' e n-1 '0'
  maxZeros = n-1
  maxOnes = 1
  for i in range(n, n+m+1):
    for j in range(1,n+1):
      if matrixAuxiliar[j][i] == 0:
        maxZeros = maxZeros-1
      elif matrixAuxiliar[j][i] == 1:
        maxOnes = maxOnes-1
      else:
        break
    else:
      if maxOnes == 0 and maxZeros == 0:
        print('pivotar coluna ', i)
        matrixAuxiliar = pivotingAuxiliar(matrixAuxiliar, n, m, i)
      maxZeros = n-1
      maxOnes = 1

  print(matrixAuxiliar)
  simplex2 = Simplex(n, m, matrixAuxiliar, matrixAuxiliar)
  simplex2.run()

else:
  print('inviavel')





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