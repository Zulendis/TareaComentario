#Clase llamada nodo
class Nodo:
    #Constructor con los argumentos
    def __init__(self,nombre,apellido,telefono,direccion,poss, izq=None, der=None):
        #Punteros
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.poss = poss
        self.izq = izq
        self.der = der

    #Retornar el valor
    def __str__(self):
        return self.poss

#Clase del arbol binario
class aBinarios:
    #metodo constructor y el atributo raiz|
    def __init__(self):
        self.raiz = None
    #creamos la funcion agregar
    def agregar(self, elemento):
        #Comparamos si la raiz esta vacia, de ser cierto añadiremos el nodo en la Raiz
        if self.raiz == None: 
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:      #Usando el While nos moveremos al siguiente nodo vacio.
                padre = aux
                if aux.izq == None: 
                        aux = aux.izq
                else:
                    if aux.der == None:
                        aux = aux.der
                    else:
                        aux= aux.izq
            if padre.izq == None:       #Una vez hemos encontrado el nodo vacio lo llenamos con la informacion del Usuario nuevo
                padre.izq = elemento
            else:
                if padre.der == None:
                    padre.der = elemento
    #Creamos la funcion que nos permitira saber en que nodo esta el Usuario               
    def Buscar(self,nombre,nodo):
        if nodo.nombre == nombre:
            return nodo.poss
        else:
            if nodo.izq != None:
                return self.Buscar(nombre,nodo.izq)
            else:
                if nodo.der != None:
                    return self.Buscar(nombre,nodo.der)
    #se crea funcion que permite obtener la raiz
    def getRaiz(self):
        return self.raiz

#creamos un menu
if __name__ == "__main__":
    #Creamos una instancia de la Clase aBinarios
    ab = aBinarios()
    poss=0
    while(True):
        #opciones del menu
        print("Arboles_Binarios\n"+
            "1. Agregar Usuario Nuevo\n"+
            "2. Buscar Usuario\n"+
            "3. Salir\n")

        num = input("Ingrese la opcion: ")

        if num == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            telefono = input("Ingrese el telefono: ")
            direccion = input("Ingrese el direccion: ")
            poss=poss+1
            nod =Nodo(nombre,apellido,telefono,direccion,poss)
            ab.agregar(nod)

        elif num == "2":
            nombre= input("Ingrese el nombre del Usuario: ")
            print("El Usuario se encuentra en la posicion: ",ab.Buscar(nombre,ab.getRaiz()))
        elif num == "3":
            exit() 