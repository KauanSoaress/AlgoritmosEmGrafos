# Import area
import sys

data = sys.stdin.readlines()
data.pop(0)
data.pop(0)
data.pop(1)

# Contar os vértices
numV = data.pop(0).split("=")
numV = int(numV[1])

# Classe para unir os componentes conexos de cada um
class UnionFind:
  def __init__(self, n):
    self.pai = list(range(n))
    self.rank = [0] * n

  def find(self, x):
    if self.pai[x] != x:
      self.pai[x] = self.find(self.pai[x])
    return self.pai[x]

  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)

    if root_x != root_y:
      if self.rank[root_x] < self.rank[root_y]:
        self.pai[root_x] = root_y
      elif self.rank[root_x] > self.rank[root_y]:
        self.pai[root_y] = root_x
      else:
        self.pai[root_y] = root_x
        self.rank[root_x] += 1

class Grafo:
  def __init__(self, numV):
    self.numV = numV
    self.grafo = []

  def constructEdgeList(self, data):
    # Fazer uma lista de arestas, ordenando pelo peso
    for i in data:
      aresta = i.rstrip("\n").split(" ")
      self.grafo.append([(int(aresta[0]) - 1), (int(aresta[1]) - 1), float(aresta[2])])

    return sorted(self.grafo, key=lambda aresta: aresta[2])

  def createCompConex(self, numv, edgeList):
    # Criação de um vetor para armazenar as arestas ao final 
    arestasFinal = []

    representantes = UnionFind(numv)

    while len(arestasFinal) != (numv - 1):
      aresta = edgeList.pop(0)
      x,y = (aresta[0],aresta[1])

      if representantes.find(x) != representantes.find(y):
        arestasFinal.append(aresta)
        representantes.union(x, y)
    return arestasFinal

  def finalWeightValue(self, arestasFinal):
    total = 0

    for i in arestasFinal:
      total += float(i[2])
    return total

grafo = Grafo(numV)
edgeList = grafo.constructEdgeList(data)
compConex = grafo.createCompConex(numV, edgeList)
print(f'{grafo.finalWeightValue(compConex):.3f}')
