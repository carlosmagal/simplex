import numpy as np
from simplex import Simplex, printOtimo, getInput, pivotingAuxiliar

def main():
  n, m, matrix, matrixAuxiliar, arrayC = getInput()

  simplex1 = Simplex(n, m+n+n, matrixAuxiliar, matrix)

  result = simplex1.runAuxiliar()#rodando simplex fase 1
  print()
  if result == 0:#otimo

    for i in range(m+n+n, n+n+n+m):# deletando coluna de variaveis auxiliares
      matrixAuxiliar = np.delete(matrixAuxiliar, n+n+m, 1)

    arrayC = arrayC * -1#multiplicando c por -1

    matrixAuxiliar[0] = arrayC #colocando c linha 0 da matriz

    maxZeros = n-1
    maxOnes = 1
    
    for i in range(n, n+n+m+1):#pivotendo a linha 0 de acordo com as bases
      for j in range(1,n+1):
        if matrixAuxiliar[j][i] == 0:
          maxZeros = maxZeros-1
        elif matrixAuxiliar[j][i] == 1:
          maxOnes = maxOnes-1
        else:
          break
      else:
        if maxOnes == 0 and maxZeros == 0:
          matrixAuxiliar = pivotingAuxiliar(matrixAuxiliar, n, n+m, i)
        maxZeros = n-1
        maxOnes = 1

    simplex2 = Simplex(n, n+m, matrixAuxiliar, matrixAuxiliar)
    
    if simplex2.run():#rodando simplex fase 2
      
      print('otima')
      print(np.around(matrixAuxiliar[0][n+n+m],7))
      # print(otimo.transpose())
      printOtimo(matrixAuxiliar, n, m+n, m)
      print(*np.around(matrixAuxiliar[0][0:n],7))

    else: 
      quit()

  elif result == 1:#inviavel
    print('inviavel')
    print(*np.around(matrixAuxiliar[0][0:n],7))

  else:#ilimitada
    quit()

main()