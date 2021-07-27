import numpy as np

class Simplex:

  def __init__(self, n, m, matrix, matrixAuxiliar):
    self.n = n
    self.m = m
    self.matrix = matrix 
    self.columnSize = m + n + 1
    self.columnSizeAuxiliar = m + n + 1
    self.matrixAuxiliar = matrixAuxiliar
    
  def isCanonical(tableau):
    return True

  def toCanonical(self):
    print(self.matrix)

  def runAuxiliar(self):
    
    while True:
      
      pivotColumn = self.getPivotColumn()
      if pivotColumn == None: 
        if(self.matrixAuxiliar[0][self.columnSizeAuxiliar-1] == 0):
          print('deu bom')
        break

      #decidindo qual vai ser o pivo
      pivotRow = self.getPivotRow(pivotColumn)
      if pivotRow == None: 
        print('nao tem nao-negativos na coluna')
        break

      self.iteration(pivotRow, pivotColumn)

#COISAS DO SIMPLEX
#negativar a primeira linha da matriz
#ver se tem negativo no b, ver se linha é toda negativa
#comecar a pivotar a partir do primeiro item negativo na matriz
#sabendo a coluna que vai ser pivotada, dividir todos os itens pelo último numero da linha
#pegar o menor e pivotar

  def run(self):
    
    # pivotColumn = self.multiplyRow(0, -1)

    while True:
      
      pivotColumn = self.getPivotColumn()
      if pivotColumn == None: 
        print('nao tem numero negativo no c')
        break

      #decidindo qual vai ser o pivo
      pivotRow = self.getPivotRow(pivotColumn)
      if pivotRow == None: 
        print('nao tem nao-negativos na coluna')
        break

      self.iteration(pivotRow, pivotColumn)
    
    print(self.matrix)

  
  def multiplyRow(self, index, multiplier):
    #multiplicando c por -1 e pegando o index da coluna pra pivotar
    #caso o pivo fique None é pq nao tem negati
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
    for i in range(self.columnSize):
      if(self.matrix[0][i] < 0 and i >= self.n):
        print(self.matrix[0][i])
        return i
    return None

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
    pivot = self.matrix[row][column]

    print(row, column)
    print(self.matrix)
    for i in range(self.n + 1):
      if i == row : continue #linha do pivo 
      else: #zerando as outras
        if self.matrix[i][column] != 0: 
          self.pivotingRow(i, row, (-1*self.matrix[i][column])/pivot)

    if pivot != 1:
      self.multiplyRow(row, 1/pivot)

    # print(self.matrix)




def auxiliar(n, m, matrix):

  for i in range(n):#multiplicando por -1, qnd b<0
    if(matrix[i][m] < 0):
      for j in range(m+1):
        matrix[i][j] = matrix[i][j] * -1

  # print(matrix)
  # print('------------------------')

  matrixWithIdentity = np.insert(matrix, m, np.identity(n), axis=1)

  arrayC = np.append(np.zeros(m),np.full((n), 1))
  arrayC = np.append(np.zeros(n), arrayC)#colocando n zeros antes do c
  arrayC = np.append(arrayC, [0])#colocando um 0 no final do c

  matrixAuxiliar = np.array(arrayC)

  identity = np.identity(n)

  for i in range(n):#tableau
    matrixAuxiliar = np.vstack([matrixAuxiliar, np.concatenate((identity[i], matrixWithIdentity[i]))])

  # print(matrixAuxiliar)


  for i in range(n+n+m+1):#pivoteando a primeira linha, pra deixar canonico
    for j in range(n+1):
      if(j == 0): continue
      matrixAuxiliar[0][i] = matrixAuxiliar[0][i] - matrixAuxiliar[j][i]

  # print(matrixAuxiliar)

  return matrixAuxiliar