import graphviz
import os

class Nodo:
    def __init__(self, Nombre, Apellido, Carnet): # NODO PRINCIPAL
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Carnet = Carnet
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_inicio(self, Nombre, Apellido, Carnet): # FUNCIÓN PARA INSERTAR DATOS AL INICIO DE LA LISTA
        nuevo_nodo = Nodo(Nombre, Apellido, Carnet)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else: 
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.visualizar()  

    def insertar_final(self, Nombre, Apellido, Carnet): # FUNCIÓN PARA INSERTAR DATOS AL FINAL DE LA LISTA
        nuevo_nodo = Nodo(Nombre, Apellido, Carnet)
        if self.cola is None:
            self.cabeza = self.cola = nuevo_nodo
        else: 
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.visualizar()  

    def eliminar(self, Nombre, Apellido, Carnet): # FUNCIÓN PARA ELIMINAR UN REGISTRO POR NOMBRE Y APELLIDO
        actual = self.cabeza
        while actual: 
            # if actual.Nombre == Nombre and actual.Apellido == Apellido:
            #     if actual.anterior:
            #         actual.anterior.siguiente = actual.siguiente
            #     else: 
            #         self.cabeza = actual.siguiente

            #     if actual.siguiente:
            #         actual.siguiente.anterior = actual.anterior
            #     else: 
            #         self.cola = actual.anterior

            #     del actual
            #     print(f"{Nombre} {Apellido} ha sido eliminado.")
            #     self.visualizar()  
            #     return
            if actual.Carnet == Carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza=actual.siguiente
                
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola=actual.anterior
                del actual
                print(f"{Nombre} {Apellido} \n{Carnet} ha sido eliminado.")
                self.visualizar()
                return
            actual = actual.siguiente
        print(f"{Nombre} {Apellido} no ha sido encontrado.")

    def mostrar(self): # FUNCIÓN PARA MOSTRAR LOS DATOS EN LA TERMINAL
        actual = self.cabeza
        print("", end=" <- ")
        while actual:
            print(f"{actual.Nombre} {actual.Apellido} {actual.Carnet}", end=" <-> \n")
            actual = actual.siguiente
        print("")

    def visualizar(self): # FUNCIÓN PARA GENERAR EL GRÁFICO DE GRAPHVIZ EN EL ESCRITORIO
        dot = graphviz.Digraph('ListaDobleEnlazada', format='png')
        actual = self.cabeza
        
        if not actual:
            print("La lista está vacía.")
            return
        
        nodo_anterior = None
        i = 1
        while actual:
            nodo_id = f'nodo{i}'
            dot.node(nodo_id, f'{actual.Nombre} {actual.Apellido} {actual.Carnet}')
            
            if nodo_anterior:
                dot.edge(nodo_anterior, nodo_id, label='siguiente')
                dot.edge(nodo_id, nodo_anterior, label='anterior')
            
            nodo_anterior = nodo_id
            actual = actual.siguiente
            i += 1
        
        ruta_guardado = os.path.expanduser(f"~/Desktop/lista_doble_enlazada")
        dot.render(ruta_guardado)
        print(f'La visualización se ha guardado como {ruta_guardado}.png')

    @staticmethod
    def pausar ():
        input("\nPresiona enter para continuar...")

# MENÚ
lista = ListaDobleEnlazada()
while True: 
    os.system("cls")
    print("----Menú----")
    print("1. Insertar al principio")
    print("2. Insertar al final")
    print("3. Eliminar por nombre y apellido")
    print("4. Mostrar lista")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        os.system("cls")
        nombre = input("Ingrese un nombre: ")
        apellido = input("Ingrese un apellido: ")
        carnet = input("Ingrese un numero de carnet: ")
        lista.insertar_inicio(nombre, apellido, carnet)
        lista.pausar()
    elif opcion == '2':
        os.system("cls")
        nombre = input("Ingrese un nombre: ")
        apellido = input("Ingrese un apellido: ")
        carnet = input("Ingrese un numero de carnet: ")
        lista.insertar_final(nombre, apellido,carnet)
        lista.pausar()
    elif opcion == '3':
        os.system("cls")
        lista.mostrar()
        carnet = input("Ingrese el numero de carnet a eliminar: ")
        lista.eliminar(nombre, apellido, carnet)
        lista.pausar()
    elif opcion == '4':
        os.system("cls")
        lista.mostrar()
        lista.pausar()
    elif opcion == '5':
        os.system("cls")
        print("Saliendo....")
        lista.pausar()
        break
    else:
        print("Opción no válida. Ingrese otra opción.")
