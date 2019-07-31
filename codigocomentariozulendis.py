"""
Una clase de Python

Esto es una clase simple de grafo en Python, demostrando la importancia
escenciales y funcionalidades de un grafo
"""


class Graph(object):

    def _init_(self, graph_dict=None):
        """ Inicializa un objeto grafo 
            si no se recibe un diccionario o se recibe None
            un diccionario vacio será usado 
            """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ retorna los vertices de un grafo """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ se recibe segmentos de un grafo """
        
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ funcion para agregar un vertice """
        
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ funcion para agregar un segmento!"""
        
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """funcion para generar segmento de uno o varios vertices"""
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def _str_(self):
"""funcion para recorrer vertices y aristas """
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


"""
 damos los puntos o valores para construir el grafo
 
"""

if _name_ == "_main_":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }


    graph = Graph(g)
   

 """ Imprimimos vertices del grafo """    
    print("Vertices of graph:")
    print(graph.vertices())

""" Imprimimos aristas del grafo """
    print("Edges of graph:")
    print(graph.edges())

""" Imprimimos agregar vertices """
    print("Add vertex:")
    graph.add_vertex("z")

""" Imprimimos vertices del grafo """
    print("Vertices of graph:")
    print(graph.vertices())

""" agregar una arista del grafo """ 
    print("Add an edge:")
    graph.add_edge({"a","z"})

""" Imprimimos vertices del grafo """    
    print("Vertices of graph:")
    print(graph.vertices())

""" Imprimimos vertices del grafo """
    print("Edges of graph:")
    print(graph.edges())

""" agregando una arista X,Y con nuevos vertices """
    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x","y"})

""" Imprimimos los nuevos vertices y aristas (X,Y) """
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
