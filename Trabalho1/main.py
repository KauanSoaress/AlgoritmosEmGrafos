import sys

# Ajusta os elementos da vizinhança de acordo com o vértice
def adjust(vert, adj_list):
  lista = []
  fila = []
  fila.append(vert)
  while len(fila) != 0:
    aux = fila.pop(0)
    for x in adj_list[aux-1]:
      if x not in lista:
        fila.append(x)
        lista.append(x)
  return sorted(lista)

# Entrada
data = sys.stdin.readlines()
data.pop(0)
data.pop(0)
data.pop(1)

# Contar os vértices
numv = data[0].split("=")
data.pop(0)
numv = int(numv[1])

# Fazer uma lista de arestas
list_arest = []
for i in data:
  aresta = i.split(" ")
  x,y = (int(aresta[0]),int(aresta[1]))
  list_arest.append((x,y))

# Criar uma lista de adjascência
adj_list = [[] for i in range(numv)]
for x, y in list_arest:
  adj_list[x-1].append(y)
  adj_list[y-1].append(x)

# Criar as componentes conexas
comp_list = []
confirm_list = [False for i in range(numv)]
for i in range(numv):
  if confirm_list[i] == False:
    aux = adjust(i+1, adj_list)
    if len(aux) != 0:
      comp_list.append(aux)
    else:
      comp_list.append([i+1])
    for x in aux:
      confirm_list[x-1] = True

# Printar as componentes conexas
for i in comp_list:
  print(" ".join(str(v) for v in i))