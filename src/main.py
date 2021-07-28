import numpy as np
from simplex import Simplex, auxiliar, printOtimo
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


def pivotingAuxiliar(matrix, n, m, column):
  if(matrix[0][column] == 0): return matrix

  for i in range( n+1):
    if(matrix[i][column] == 1):#pegando index da linha do pivo
      multiplier = -1 * matrix[0][column]
      for j in range(n+m+1):
        matrix[0][j] = matrix[0][j] + (multiplier*matrix[i][j])
        
  
  return matrix
##################################

n, m, matrix, matrixAuxiliar, arrayC = getInput()

simplex1 = Simplex(n, m+n, matrixAuxiliar, matrix)

#0 otimo
#1 inviavel
#2 ilimitada
result = simplex1.runAuxiliar()#rodando simplex fase 1

if result == 0:

  for i in range(m+n, n+n+m):# deletando coluna de variaveis auxiliares
    matrixAuxiliar = np.delete(matrixAuxiliar, n+m, 1)

  for i in range(n):#deletando vero da auxiliar
    matrixAuxiliar = np.delete(matrixAuxiliar, 0, 1)

  matrixAuxiliar = np.append(np.vstack([np.zeros(n), np.identity(n)]), matrixAuxiliar, axis=1)#colocando novo vero na matriz

  arrayC = arrayC * -1#multiplicando c por -1

  matrixAuxiliar[0] = arrayC #colocando c linha 0 da matriz

  maxZeros = n-1
  maxOnes = 1
  
  for i in range(n, n+m+1):#pivotendo a linha 0 de acordo com as bases
    for j in range(1,n+1):
      if matrixAuxiliar[j][i] == 0:
        maxZeros = maxZeros-1
      elif matrixAuxiliar[j][i] == 1:
        maxOnes = maxOnes-1
      else:
        break
    else:
      if maxOnes == 0 and maxZeros == 0:
        matrixAuxiliar = pivotingAuxiliar(matrixAuxiliar, n, m, i)
      maxZeros = n-1
      maxOnes = 1

  simplex2 = Simplex(n, m, matrixAuxiliar, matrixAuxiliar)
  
  if simplex2.run():#rodando simplex fase 2
  
    print('otima')
    print(np.around(matrixAuxiliar[0][n+m],7))
    # print(otimo.transpose())
    printOtimo(matrixAuxiliar, n, m)
    print(np.around(matrixAuxiliar[0][0:n],7))

  else: 
    print('ilimitada')
    printOtimo(matrixAuxiliar, n, m)
    print(np.around(matrixAuxiliar[0][0:n],7))


elif result == 1:
  print('inviavel')
  print(np.around(matrixAuxiliar[0][0:n],7))

else:
  print('ilimitada')
  printOtimo(matrixAuxiliar, n, m)
  print(np.around(matrixAuxiliar[0][0:n],7))