# Import area
import sys

data = sys.stdin.readlines()

class Node:
  def __init__(self, value):
    self.value = value
    self.prox = None

class LinkedList:
  def __init__(self):
    self.primeiro = None
    self.ultimo = None
    self.tam = 0
  

class Grafo:
  def __init__(self, data):
    self.data = data

  def countVert(self):
    self.data.pop(0)
    self.data.pop(0)
    self.data.pop(1)

    # Contar os vértices
    aux = data.pop(0).split("=")
    self.numV = int(aux[1])

    return self.numV
  
  def edgesOrder(self):
    arestasOrdenadas = []

    for i in self.data:
      aresta = i.rstrip("\n").split(" ")
      arestasOrdenadas.append([(int(aresta[0]) - 1), (int(aresta[1]) - 1), float(aresta[2])])
    return sorted(arestasOrdenadas, key=lambda aresta: aresta[2])
  
  def createAGM(self, numV, orderedEdges):

    representantes = []
    compsConex = []
    for i in range(numV):
      compsConex.append(LinkedList())
      compsConex[i].primeiro = Node(i)
      compsConex[i].ultimo = compsConex[i].primeiro
      compsConex[i].tam = 1
      representantes.append(i)

    agm = []
    while len(agm) != (numV-1):

      edge = orderedEdges.pop(0)
      u = representantes[edge[0]]
      v = representantes[edge[1]]

      if u != v:
        agm.append(edge)
        x = u
        y = v
        if compsConex[x].tam < compsConex[y].tam:
          aux = x
          x = y
          y = aux
        z = compsConex[y].primeiro
        compsConex[x].ultimo.prox = z
        compsConex[x].ultimo = compsConex[y].ultimo
        compsConex[x].tam += compsConex[y].tam
        while z != None:
          representantes[z.value] = x
          z = z.prox

    total = 0

    for i in agm:
      total += float(i[2])

    return total  


grafo = Grafo(data)
numV = grafo.countVert()
orderedEdges = grafo.edgesOrder()
agm = grafo.createAGM(numV, orderedEdges)
print(f'{agm:.3f}')