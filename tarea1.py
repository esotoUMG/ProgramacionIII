import graphviz
import os

class Nodo:
    def __init__(self, Nombre, Apellido):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.siguiente = None
        self.anterior = None

class lista_doble_enlazada:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarinicio(self, Nombre, Apellido):
        nodonuevo = Nodo(Nombre, Apellido)
        if self.cabeza is None:
            self.cabeza = self.cola = nodonuevo
        else: 
            nodonuevo.siguiente = self.cabeza
            self.cabeza.anterior = nodonuevo
            self.cabeza = nodonuevo
        self.visualizar()  

    def insertarfinal(self, Nombre, Apellido):
        nodonuevo = Nodo(Nombre, Apellido)
        if self.cola is None:
            self.cabeza = self.cola = nodonuevo
        else: 
            self.cola.siguiente = nodonuevo
            nodonuevo.anterior = self.cola
            self.cola = nodonuevo
        self.visualizar()  

    def eliminar(self, Nombre, Apellido):
        actual = self.cabeza
        while actual: 
            if actual.Nombre == Nombre and actual.Apellido == Apellido:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else: 
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else: 
                    self.cola = actual.anterior

                del actual
                print(f"{Nombre} {Apellido} ha sido eliminado.")
                self.visualizar()  
                return

            actual = actual.siguiente
        
        print(f"{Nombre} {Apellido} no ha sido encontrado.")

    def mostrar(self):
        actual = self.cabeza
        print("", end=" <- ")
        while actual:
            print(f"{actual.Nombre} {actual.Apellido}", end=" <-> ")
            actual = actual.siguiente
        print("")

    def visualizar(self):
        dot = graphviz.Digraph('ListaDobleEnlazada', format='png')
        actual = self.cabeza
        
        if not actual:
            print("La lista está vacía.")
            return
        
        prev_node = None
        i = 1
        while actual:
            node_id = f'nodo{i}'
            dot.node(node_id, f'{actual.Nombre} {actual.Apellido}')
            
            if prev_node:
                dot.edge(prev_node, node_id, label='siguiente')
                dot.edge(node_id, prev_node, label='anterior')
            
            prev_node = node_id
            actual = actual.siguiente
            i += 1
        
        ruta_guardado = os.path.expanduser(f"~/Desktop/lista_doble_enlazada")
        dot.render(ruta_guardado)
        print(f'La visualización se ha guardado como {ruta_guardado}.png')

# MENU
lista = lista_doble_enlazada()
while True: 
    print("\n----Menú----")
    print("1. Insertar al principio")
    print("2. Insertar al final")
    print("3. Eliminar por nombre y apellido")
    print("4. Mostrar lista")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        nombre = input("Ingrese un nombre: ")
        apellido = input("Ingrese un apellido: ")
        lista.insertarinicio(nombre, apellido)
    elif opcion == '2':
        nombre = input("Ingrese un nombre: ")
        apellido = input("Ingrese un apellido: ")
        lista.insertarfinal(nombre, apellido)
    elif opcion == '3':
        nombre = input("Ingrese el nombre a eliminar: ")
        apellido = input("Ingrese el apellido a eliminar: ")
        lista.eliminar(nombre, apellido)
    elif opcion == '4':
        lista.mostrar()
    elif opcion == '5':
        print("Saliendo....")
        break
    else:
        print("Opción no válida. Ingrese otra opción.")
