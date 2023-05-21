# Import area
import sys

class UnionFind:
  def __init__(self, vertices):
    self.parent = list(range(vertices))
    self.rank = [0] * vertices

  def find(self, v):
    if self.parent[v] != v:
      self.parent[v] = self.find(self.parent[v])
    return self.parent[v]

  def union(self, v1, v2):
    root1 = self.find(v1)
    root2 = self.find(v2)

    if root1 != root2:
      if self.rank[root1] < self.rank[root2]:
        self.parent[root1] = root2
      elif self.rank[root1] > self.rank[root2]:
        self.parent[root2] = root1
      else:
        self.parent[root2] = root1
        self.rank[root1] += 1

class Node:
  def __init__(self, value):
    self.value = value
    self.prox = None

class LinkedList:
  def __init__(self):
    self.primeiro = None
    self.ultimo = None
    
  def append(self, value):
    newNode = Node(value)

    if self.primeiro == None:
      self.primeiro = newNode
      self.ultimo = newNode
    else:
      self.ultimo.prox = newNode
      self.ultimo = newNode
  
class Edge:
  def __init__(self, aresta):
    self.u = aresta[0]
    self.v = aresta[1]
    self.weight = aresta[2]

class Grafo:
  def __init__(self, numV):
    self.numV = numV
    self.arestas = LinkedList()
  
  def addEdge(self, arestas):
    for i in arestas:
      self.arestas.append(Edge(i))

  def kruskal(self, numV):
    representantes = UnionFind(numV)
    agm = []

    currentEdge = self.arestas.primeiro

    while len(agm) != (numV - 1):
      u = currentEdge.value.u
      v = currentEdge.value.v

      reprU = representantes.find(u)
      reprV = representantes.find(v)

      if reprU != reprV:
        agm.append(currentEdge.value)
        representantes.union(reprU, reprV)
    return agm
  

data = sys.stdin.readlines()
data.pop(0)
data.pop(0)
data.pop(1)

# Contar os vértices
numV = data.pop(0).split("=")
numV = int(numV[1])

arestas = []
for i in data:
  aresta = i.rstrip("\n").split(" ")
  arestas.append([(int(aresta[0]) - 1), (int(aresta[1]) - 1), float(aresta[2])])
arestas = sorted(arestas, key=lambda aresta: aresta[2])

grafo = Grafo(numV)
grafo.addEdge(arestas)

agm = grafo.kruskal(numV)