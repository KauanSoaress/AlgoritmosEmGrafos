Trabalho 2 - Árvore Geradora Mínima

Escreva um programa que compute o peso de uma Árvore Geradora Mínima do grafo recebido como entrada.

Formato da Entrada
A entrada, recebida através da entrada padrão, estará no formato UCINET DL, lista de arestas ("edgelist1"), sem rótulos para os vértices mas com pesos para as arestas, conforme o seguinte exemplo:

dl
format=edgelist1
n=4
data:
2 4 -61.500
1 3 83.750
1 2 -29.500
3 4 78.000
2 3 5.125

Observe que, no formato acima, os vértices são numerados a partir de 1.

Formato da Saída
A saída, fornecida através da saída padrão, tem que estar no formato ilustrado pelo seguinte exemplo, que é a saída esperada para a entrada acima:

-85.875

Ou seja, a saída deve possuir apenas uma linha, que possuirá apenas um número: o peso da AGM, escrito COM EXATAMENTE 3 CASAS DECIMAIS.