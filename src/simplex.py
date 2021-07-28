import numpy as np

class Simplex:

  def __init__(self, n, m, matrix, matrixAuxiliar):
    self.n = n
    self.m = m
    self.matrix = matrix 
    self.columnSize = m + n + 1
    self.matrixAuxiliar = matrixAuxiliar
    self.columnSizeAuxiliar = m + n + 1

  def runAuxiliar(self):#fase 1
    print('\n\n')
    while True:
      #selecionando coluna para ser pivoteada
      pivotColumn = self.getPivotColumn()
      if pivotColumn == None: 
        if(np.isclose(self.matrix[0][self.columnSizeAuxiliar-1], 0)):
          return 0
        else:
          return 1

      #selecionando linha do pivo
      pivotRow = self.getPivotRow(pivotColumn)
      if pivotRow == None: 
        return 2

      #pivotenado
      self.iteration(pivotRow, pivotColumn)

  def run(self):#fase 2

    while True:
      #coluna do pivo
      pivotColumn = self.getPivotColumn()
      if pivotColumn == None: 
        return True

      #linha do pivo
      pivotRow = self.getPivotRow(pivotColumn)
      if pivotRow == None: 
        return False

      #pivoteando
      self.iteration(pivotRow, pivotColumn)
    

  def multiplyRow(self, index, multiplier):
    pivotIndex = None
    for i in range(self.columnSize):
      if(self.matrix[index][i] != 0):
        self.matrix[index][i] = self.matrix[index][i] * multiplier
        if(self.matrix[index][i] < 0 and i >= self.n and pivotIndex == None):
          pivotIndex = i

    return pivotIndex
  
  def pivotingRow(self, index, index2, multiplier):
    for i in range(self.columnSize):
      self.matrix[index][i] = self.matrix[index][i] + ( multiplier * self.matrix[index2][i])
  
  def getPivotColumn(self):
    lower = 1000000
    pivotColumn = None
    for i in range(self.columnSize-1):
      if(self.matrix[0][i] < 0 and i >= self.n):
        return i

    return pivotColumn

  def getPivotRow(self, column):
    lowerRatio = float('inf')
    pivotAxis = None

    for i in range(self.n + 1):
      if i == 0 or self.matrix[i][column] <= 0: continue

      currentRatio = self.matrix[i][self.columnSize-1] / self.matrix[i][column]

      if currentRatio < lowerRatio:
        lowerRatio = currentRatio
        pivotAxis = i
    
    return pivotAxis

  def iteration(self, row, column):
    pivot = self.matrix[row][column]

    for i in range(self.n + 1):
      if i == row : continue #linha do pivo 
      else: #zerando as outras
        if self.matrix[i][column] != 0: 
          self.pivotingRow(i, row, (-1*self.matrix[i][column])/pivot)

    if pivot != 1:
      self.multiplyRow(row, 1/pivot)




def auxiliar(n, m, matrix):

  for i in range(n):#multiplicando por -1, qnd b<0
    if(matrix[i][m] < 0):
      for j in range(m+1):
        matrix[i][j] = matrix[i][j] * -1

  matrixWithIdentity = np.insert(matrix, m, np.identity(n), axis=1)

  arrayC = np.append(np.zeros(m),np.full((n), 1))
  arrayC = np.append(np.zeros(n), arrayC)#colocando n zeros antes do c
  arrayC = np.append(arrayC, [0])#colocando um 0 no final do c

  matrixAuxiliar = np.array(arrayC)

  identity = np.identity(n)

  for i in range(n):#tableau
    matrixAuxiliar = np.vstack([matrixAuxiliar, np.concatenate((identity[i], matrixWithIdentity[i]))])
  
  for i in range(n+n+m+1):#pivoteando a primeira linha, pra deixar canonico
    for j in range(n+1):
      if(j == 0): continue
      matrixAuxiliar[0][i] = matrixAuxiliar[0][i] - matrixAuxiliar[j][i]

  return matrixAuxiliar


def printOtimo(matrix, n, m):
  maxZeros = n-1
  maxOnes = 1

  otimo = np.array([])

  for i in range(n, n+m):
    if matrix[0][i] != 0:
      otimo = np.append(otimo, [0])
      continue
    else:
      maxZeros = n-1
      maxOnes = 1
      rowIndex = 0
      for j in range(1, n+1):
        if matrix[j][i] == 0:
          maxZeros = maxZeros-1
        elif matrix[j][i] == 1:
          maxOnes = maxOnes-1
          rowIndex = j
        else:
          otimo = np.append(otimo, [0])
          break
      else:
        if maxOnes == 0 and maxZeros == 0:# se for base
          otimo = np.append(otimo,matrix[rowIndex][n+m])
        else:
          otimo = np.append(otimo, [0])
        
  print(np.around(otimo,7))