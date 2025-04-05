import os
import graphviz
import csv

# Nodo básico del árbol binario de búsqueda
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1  # Requerido para el árbol AVL

# Árbol binario de búsqueda
class ABB:
    def __init__(self):
        self.Raiz = None

    def agregar(self, valor, nodo):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self.agregar(valor, nodo.izq)
        elif valor > nodo.valor:
            nodo.der = self.agregar(valor, nodo.der)
        return nodo

    def encontrar(self, valor, nodo):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self.encontrar(valor, nodo.izq)
        else:
            return self.encontrar(valor, nodo.der)

    def encontrarmenor(self, nodo):
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    def eliminar(self, valor, nodo):
        if nodo is None:
            print(f"El nodo {valor} no existe en el árbol.")
            return nodo
        if valor < nodo.valor:
            nodo.izq = self.eliminar(valor, nodo.izq)
        elif valor > nodo.valor:
            nodo.der = self.eliminar(valor, nodo.der)
        else:
            if nodo.izq is None and nodo.der is None:
                return None
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            sucesor = self.encontrarmenor(nodo.der)
            nodo.valor = sucesor.valor
            nodo.der = self.eliminar(sucesor.valor, nodo.der)
        return nodo

    def generar_dot(self):
        if not self.Raiz:
            print("El árbol está vacío.")
            return None

        dot = graphviz.Digraph('ArbolBinarioBusquedaAVL', format='png')

        def agregar_nodos(nodo):
            if nodo:
                nodo_id = str(nodo.valor)
                dot.node(nodo_id, str(nodo.valor))
                if nodo.izq:
                    dot.edge(nodo_id, str(nodo.izq.valor), label="Izq")
                    agregar_nodos(nodo.izq)
                if nodo.der:
                    dot.edge(nodo_id, str(nodo.der.valor), label="Der")
                    agregar_nodos(nodo.der)

        agregar_nodos(self.Raiz)
        return dot

    def guardar_visualizacion(self):
        dot = self.generar_dot()
        if dot:
            ruta_guardado = os.path.expanduser(f"~/Desktop/AVL")
            dot.render(ruta_guardado, format="png", cleanup=True)
            print(f'Se ha guardado la visualización como {ruta_guardado}.png')

    def archivoCSV(self, nombreArchivo):
        try:
            with open(nombreArchivo, newline='', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                valores_cargados = 0
                for fila in lector:
                    for valor in fila:
                        try:
                            numero = int(valor)
                            self.Raiz = self.agregar(numero, self.Raiz)
                            valores_cargados += 1
                        except ValueError:
                            print(f"Valor inválido en CSV: {valor}. Se omitirá.")
            if valores_cargados > 0:
                print(f"Se han agregado {valores_cargados} valores desde el archivo CSV.")
            else:
                print("No se encontraron valores válidos en el archivo.")
        except FileNotFoundError:
            print(f"No se encontró el archivo en {nombreArchivo}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

# Árbol AVL hereda de ABB
class AVL(ABB):
    def obtenerAltura(self, nodo):
        return nodo.altura if nodo else 0

    def obtenerBalance(self, nodo):
        return self.obtenerAltura(nodo.izq) - self.obtenerAltura(nodo.der) if nodo else 0

    def rotacionDerecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self.obtenerAltura(y.izq), self.obtenerAltura(y.der))
        x.altura = 1 + max(self.obtenerAltura(x.izq), self.obtenerAltura(x.der))
        return x

    def rotacionIzquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self.obtenerAltura(x.izq), self.obtenerAltura(x.der))
        y.altura = 1 + max(self.obtenerAltura(y.izq), self.obtenerAltura(y.der))
        return y

    def agregar(self, valor, nodo):
        if not nodo:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self.agregar(valor, nodo.izq)
        elif valor > nodo.valor:
            nodo.der = self.agregar(valor, nodo.der)
        else:
            return nodo

        nodo.altura = 1 + max(self.obtenerAltura(nodo.izq), self.obtenerAltura(nodo.der))
        balance = self.obtenerBalance(nodo)

        if balance > 1 and valor < nodo.izq.valor:
            return self.rotacionDerecha(nodo)
        if balance < -1 and valor > nodo.der.valor:
            return self.rotacionIzquierda(nodo)
        if balance > 1 and valor > nodo.izq.valor:
            nodo.izq = self.rotacionIzquierda(nodo.izq)
            return self.rotacionDerecha(nodo)
        if balance < -1 and valor < nodo.der.valor:
            nodo.der = self.rotacionDerecha(nodo.der)
            return self.rotacionIzquierda(nodo)

        return nodo

    def eliminar(self, valor, nodo):
        if not nodo:
            print(f"El nodo {valor} no existe en el árbol.")
            return nodo

        if valor < nodo.valor:
            nodo.izq = self.eliminar(valor, nodo.izq)
        elif valor > nodo.valor:
            nodo.der = self.eliminar(valor, nodo.der)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            temp = self.encontrarmenor(nodo.der)
            nodo.valor = temp.valor
            nodo.der = self.eliminar(temp.valor, nodo.der)

        nodo.altura = 1 + max(self.obtenerAltura(nodo.izq), self.obtenerAltura(nodo.der))
        balance = self.obtenerBalance(nodo)

        if balance > 1 and self.obtenerBalance(nodo.izq) >= 0:
            return self.rotacionDerecha(nodo)
        if balance > 1 and self.obtenerBalance(nodo.izq) < 0:
            nodo.izq = self.rotacionIzquierda(nodo.izq)
            return self.rotacionDerecha(nodo)
        if balance < -1 and self.obtenerBalance(nodo.der) <= 0:
            return self.rotacionIzquierda(nodo)
        if balance < -1 and self.obtenerBalance(nodo.der) > 0:
            nodo.der = self.rotacionDerecha(nodo.der)
            return self.rotacionIzquierda(nodo)

        return nodo

arbol_global = None

def limpiar_final():
    global arbol_global
    arbol_global = None

    escritorio = os.path.expanduser("~/Desktop")
    prefijo = "AVL"
    extensiones = [".png", ".gv", ".gv.pdf", ".gv.svg"]

    for ext in extensiones:
        ruta = os.path.join(escritorio, prefijo + ext)
        if os.path.exists(ruta):
            os.remove(ruta)

class MenuABB:
    @staticmethod
    def menuPrincipal():
        os.system("cls" if os.name == "nt" else "clear")
        print("Bienvenido al programa de Árboles (AVL incluido)\n")
        print("-------------------------------------------:")
        print("Por favor indique qué desea hacer:")
        print("-------------------------------------------:")
        print("1) Insertar número en el árbol")
        print("2) Buscar un número en el árbol")
        print("3) Eliminar un número del árbol")
        print("4) Cargar un árbol desde un archivo CSV")
        print("5) Visualizar el árbol mediante Graphviz")
        print("6) Salir")

    @staticmethod
    def pausar():
        input("\nPresiona enter para continuar...")

    @staticmethod
    def cls():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def opcion1():
        MenuABB.cls()
        print("------INSERTAR NODO------")
        print("Ingrese un número (o escriba 'salir' para terminar):")
        while True:
            valor = input()
            if valor.lower() == 'salir':
                break
            if valor.isdigit():
                numero = int(valor)
                global arbol_global
                arbol_global.Raiz = arbol_global.agregar(numero, arbol_global.Raiz)
                print(f"Nodo {numero} agregado correctamente.")
            else:
                print(f"'{valor}' no es un número válido.")
            print("Agregue otro número o escriba 'salir':")

    @staticmethod
    def opcion2():
        MenuABB.cls()
        print("------BUSCAR NODO------")
        valor = input("Ingrese el nodo que desea buscar en el árbol: ")
        if valor.isdigit():
            numero = int(valor)
            global arbol_global
            encontrado = arbol_global.encontrar(numero, arbol_global.Raiz)
            if encontrado:
                print(f"Nodo {numero} encontrado en el árbol.")
            else:
                print(f"El nodo {numero} no se encuentra en el árbol.")
        else:
            print(f"'{valor}' no es un número válido.")
        MenuABB.pausar()

    @staticmethod
    def opcion3():
        MenuABB.cls()
        print("------ELIMINAR NODO------")
        valor = input("Ingrese el nodo que desea eliminar: ")
        if valor.isdigit():
            numero = int(valor)
            global arbol_global
            arbol_global.Raiz = arbol_global.eliminar(numero, arbol_global.Raiz)
            print(f"Nodo {numero} eliminado correctamente.")
        else:
            print(f"'{valor}' no es un número válido.")
        MenuABB.pausar()

    @staticmethod
    def opcion4():
        MenuABB.cls()
        print("------CARGAR DATOS DESDE ARCHIVO------")
        global arbol_global
        arbol_global.archivoCSV("CSVTarea1000.csv")

    @staticmethod
    def opcion5():
        MenuABB.cls()
        print("------VISUALIZAR ÁRBOL------")
        global arbol_global
        arbol_global.guardar_visualizacion()
        MenuABB.pausar()

    @staticmethod
    def opcion6():
        MenuABB.cls()
        print("Saliendo del programa...")
        limpiar_final()
        exit()

def reiniciar_estado():
    global arbol_global
    arbol_global = AVL()

    escritorio = os.path.expanduser("~/Desktop")
    prefijo = "AVL"
    extensiones = [".png", ".gv", ".gv.pdf", ".gv.svg"]

    for ext in extensiones:
        ruta = os.path.join(escritorio, prefijo + ext)
        if os.path.exists(ruta):
            os.remove(ruta)

def menu():
    while True:
        MenuABB.menuPrincipal()
        seleccion = input("Seleccione una opción (1-6): ")
        if seleccion == '1':
            MenuABB.opcion1()
        elif seleccion == '2':
            MenuABB.opcion2()
        elif seleccion == '3':
            MenuABB.opcion3()
        elif seleccion == '4':
            MenuABB.opcion4()
        elif seleccion == '5':
            MenuABB.opcion5()
        elif seleccion == '6':
            MenuABB.opcion6()
        else:
            MenuABB.cls()
            print("Por favor seleccione una opción válida")
            MenuABB.pausar()

reiniciar_estado()
menu()