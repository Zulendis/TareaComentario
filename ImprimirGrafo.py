class Vertice:
    def __init__(self, n):
        self.nombre = n


class Grafo:
    vertices = {}
    bordes = []
    indices_bordes = {}

    def agregar_vertice(self, vertex):
        if isinstance(vertex, Vertice) and vertex.nombre not in self.vertices:
            self.vertices[vertex.nombre] = vertex
            for fila in self.bordes:
                fila.append(0)
            self.bordes.append([0] * (len(self.bordes) + 1))
            self.indices_bordes[vertex.nombre] = len(self.indices_bordes)
            return True
        else:
            return False

    def agregar_borde(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.bordes[self.indices_bordes[u]][self.indices_bordes[v]] = weight
            self.bordes[self.indices_bordes[v]][self.indices_bordes[u]] = weight
            return True
        else:
            return False

    def imprimir_grafo(self):
        for v, x in sorted(self.indices_bordes.items()):
            print(v + ' ', end='')
            for j in range(len(self.bordes)):
                print(self.bordes[x][j], end='')
            print(' ')


g = Grafo()

a = Vertice('1')
g.agregar_vertice(a)
g.agregar_vertice(Vertice('2'))
for i in range(ord('1'), ord('8')):
    g.agregar_vertice(Vertice(chr(i)))

bordes = ['12', '24', '26', '43', '32', '45', '52', '65', '67', '75', '74']

for borde in bordes:
    g.agregar_borde(borde[:1], borde[1:])

g.imprimir_grafo()