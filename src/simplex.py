import numpy as np

class Simplex:

  def __init__(self, n, m, matrix, matrixAuxiliar):
    self.n = n
    self.m = m
    self.matrix = matrix 
    self.columnSize = m + n + 1
    self.matrixAuxiliar = matrixAuxiliar
    self.columnSizeAuxiliar = m + n + 1

  def runAuxiliar(self):
    
    while True:
      
      pivotColumn = self.getPivotColumn()
      if pivotColumn == None: 
        print(self.matrix[0][self.columnSizeAuxiliar-1])
        print('----------------')
        print(self.matrix)
        if(np.isclose(self.matrix[0][self.columnSizeAuxiliar-1], 0)):
          return True
        else:
          return False

      pivotRow = self.getPivotRow(pivotColumn)
      if pivotRow == None: 
        return False

      self.iteration(pivotRow, pivotColumn)

  def run(self):
    print('TA NO RUN----------------')
    # pivotColumn = self.multiplyRow(0, -1)

    while True:
      
      pivotColumn = self.getPivotColumn()
      if pivotColumn == None: 
        print(self.matrix)
        return True

      pivotRow = self.getPivotRow(pivotColumn)
      if pivotRow == None: 
        print('nao tem nao-negativos na coluna')
        print(self.matrix)
        return False

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
        # if lower >= self.matrix[0][i]:
        #   lower = self.matrix[0][i]
        # pivotColumn = i
        print(self.matrix[0][i])
        return i

    # print('pivo: ', pivotColumn)
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

  # o iteration vai fazer a pivotação
  # vai ser chamado na runSimplex equanto nao tiver resultado
  def iteration(self, row, column):
    # self.matrix = np.around(self.matrix,3)
    pivot = self.matrix[row][column]

    print(row, column)
    print(np.round(self.matrix,2))
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
  print(matrixAuxiliar)
  print('em cima')
  for i in range(n+n+m+1):#pivoteando a primeira linha, pra deixar canonico
    for j in range(n+1):
      if(j == 0): continue
      matrixAuxiliar[0][i] = matrixAuxiliar[0][i] - matrixAuxiliar[j][i]
  print(matrixAuxiliar)
  # quit()
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
        
        # maxZeros = n-1
        # maxOnes = 1
  
  print(np.around(otimo,7))