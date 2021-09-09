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
    # print('\n\n')
    while True:
      #selecionando coluna para ser pivoteada

      if self.isUnlimited(self.n, self.columnSize-1):
        return -1

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

      #pivoteando
      self.iteration(pivotRow, pivotColumn)

  def run(self):#fase 2
    #EM TODA EXECUCAO TENHO Q CHECAR SE ELA É ILIMITADA,
    #ELE PODE TER A LINHA TODA NEGATIVA EM UMA COLUNA DIFERENTE DA DO PIVO
    while True:
      
      #checa se é ilimitada
      if self.isUnlimited(self.n, self.columnSize-1):
        print('aaaaaaaaaaaaaaa')
        return False

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
    lower = -1000000
    pivotColumn = None
    for i in range(self.columnSize-1):
      if(self.matrix[0][i] < 0 and self.matrix[0][i] > lower and i >= self.n):
        return i
        lower = self.matrix[0][i]
        pivotColumn = i

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

  def isUnlimited(self, n, limit):
    for j in range(n, limit):
      if self.matrix[0][j] < 0:
        unlimited = True
        for i in range(1, n+1):
          if self.matrix[i][j] > 0:
            unlimited = False
        
        if unlimited:
          return True

    return False



#monta a pl auxiliar
def auxiliar(n, m, matrix):

  matrix = np.concatenate((np.identity(n), matrix), axis=1)

  for i in range(n):#multiplicando por -1, qnd b<0
    if(matrix[i][m+n] < 0):
      for j in range(m+n+1):
        matrix[i][j] = matrix[i][j] * -1

  matrixWithIdentity = np.insert(matrix, m+n, np.identity(n), axis=1)

  arrayC = np.append(np.zeros(m),np.full((n), 1))
  arrayC = np.append(np.zeros(n), arrayC)#colocando n zeros antes do c
  arrayC = np.append(arrayC, [0])#colocando um 0 no final do c

  matrixAuxiliar = np.vstack([arrayC,matrixWithIdentity])

  for i in range(n+n+m+1):#pivoteando a primeira linha, pra deixar canonico
    for j in range(n+1):
      if(j == 0): continue
      matrixAuxiliar[0][i] = matrixAuxiliar[0][i] - matrixAuxiliar[j][i]

  return matrixAuxiliar

#printa o otimo
def printOtimo(matrix, n, m, limit):
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
        
  print(*np.around(otimo[0:limit],7))


#input
def getInput():
  n, m = map(int, input().split())

  arrayC = np.array([input().strip().split()], float)#pegando o c normal
  arrayC = np.append(np.zeros(n), arrayC)#colocando n zeros antes do c
  arrayC = np.append(arrayC, np.zeros(n+1))#colocando um 0 no final do c

  matrixInput = np.array([input().strip().split() for _ in range(n)], int)
  matrixInput = np.insert(matrixInput, m, np.identity(n), axis = 1)#deixando canonico(Ax=b)

  matrixAuxiliar = auxiliar(n, n+m, matrixInput)

  identity = np.identity(n)
  matrix = np.array(arrayC)

  for i in range(n):#tableau
    matrix = np.vstack([matrix, np.concatenate((identity[i],matrixInput[i]))])

  return n, m, matrix, matrixAuxiliar, arrayC

#pivoteamento da pl auxiliar
def pivotingAuxiliar(matrix, n, m, column):
  if(matrix[0][column] == 0): return matrix

  for i in range( n+1):
    if(matrix[i][column] == 1):#pegando index da linha do pivo
      multiplier = -1 * matrix[0][column]
      for j in range(n+m+1):
        matrix[0][j] = matrix[0][j] + (multiplier*matrix[i][j])

  return matrix