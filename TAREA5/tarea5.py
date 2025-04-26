import os
import graphviz
import csv
import math

ArbolGlobal = None

#CLASE NODO
class Nodo:
    def __init__(self, grado, hoja=False):
        self.grado = grado
        self.hoja = hoja
        self.claves = []
        self.hijos = []

#CLASE ARBOL B
class Btree:
    def __init__(self, grado):
        self.grado = grado
        self.raiz = Nodo(grado, True)
        self.max_claves = grado - 1 #formula para calcular maximo de claves
        self.min_claves = math.ceil((grado + 1) / 2) - 1 #formula para calcular minimo de claves

    #METODOS PARA INSERTAR DENTRO DEL ARBOL
    def dividirHijo(self, padre, i):
        grado = self.grado
        y = padre.hijos[i]
        z = Nodo(grado, y.hoja)

        if grado % 2 == 0:
            medio = (grado // 2) - 1
        else:
            medio = (grado - 1) // 2

        padre.claves.insert(i, y.claves[medio])
        padre.hijos.insert(i + 1, z)

        z.claves = y.claves[medio + 1:]
        y.claves = y.claves[:medio]

        if not y.hoja:
            z.hijos = y.hijos[medio + 1:]
            y.hijos = y.hijos[:medio + 1]

    def _insertar_post_division(self, nodo, k):
        i = len(nodo.claves) - 1
        if nodo.hoja:
            nodo.claves.append(None)
            while i >= 0 and k < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = k
        else:
            while i >= 0 and k < nodo.claves[i]:
                i -= 1
            i += 1
            self._insertar_post_division(nodo.hijos[i], k)
            if len(nodo.hijos[i].claves) > self.max_claves:
                self.dividirHijo(nodo, i)

    def agregar(self, k):
        raiz = self.raiz
        self._insertar_post_division(raiz, k)
        if len(self.raiz.claves) > self.max_claves:
            s = Nodo(self.grado, False)
            s.hijos.append(self.raiz)
            self.dividirHijo(s, 0)
            self.raiz = s

    #METODO PARA BUSCAR NODO DENTRO DE ARBOL
    def buscar(self, k, nodo=None):
        if nodo is None:
            nodo = self.raiz
        i = 0
        while i < len(nodo.claves) and k > nodo.claves[i]:
            i += 1
        if i < len(nodo.claves) and nodo.claves[i] == k:
            return True
        if nodo.hoja:
            return False
        return self.buscar(k, nodo.hijos[i])

    #METODO PARA AGREGAR NODOS A GRAPHVIZ
    def agregar_nodos(self, nodo, dot):
        idActual = f"nodo{id(nodo)}"
        label = " | ".join(str(clave) for clave in nodo.claves)
        dot.node(idActual, label, shape='box')

        for hijo in nodo.hijos:
            idHijo = f"nodo{id(hijo)}"
            self.agregar_nodos(hijo, dot)
            dot.edge(idActual, idHijo)

    def generar_visualizacion(self):
        dot = graphviz.Digraph('ArbolB')
        self.agregar_nodos(self.raiz, dot)
        ruta_guardado = os.path.expanduser("ArbolB")
        dot.render(ruta_guardado, format="png", cleanup=True, view=True)
        print(f"\nSe ha guardado la visualización como {ruta_guardado}.png")

    #METODO PARA CARGAR ARCHIVO CSV
    def archivoCSV(self, nombreArchivo):
        try:
            print(f"Ruta absoluta del archivo: {os.path.abspath(nombreArchivo)}")
            with open(nombreArchivo, newline='', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                valores_cargados = 0
                for fila in lector:
                    for valor in fila:
                        try:
                            numero = int(valor)
                            self.agregar(numero)
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
        self.generar_visualizacion()


# MENU PRINCIPAL Y OPERACIONES
class MenuAB:
    @staticmethod
    def menuPrincipal():#VISION GENERAL DEL MENU PRINCIPAL
        os.system("cls" if os.name == "nt" else "clear")
        print("Bienvenido al programa del árbol B")
        print("-------------------------------------------")
        print("Por favor indique qué desea hacer:")
        print("-------------------------------------------")
        print("1. Ingrese el grado del árbol")
        print("2. Operaciones básicas")
        print("3. Cargar datos desde archivo CSV")
        print("4. Generar gráfico en Graphviz")
        print("5. Salir")

    @staticmethod
    def pausar():
        input("\nPresiona enter para continuar...")

    @staticmethod
    def cls():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def opcion1(): #INGRESAR EL GRADO DEL ARBOL
        MenuAB.menuPrincipal()
        global ArbolGlobal
        print("-------ESTABLECER GRADO-------")
        grado = int(input("Ingrese el grado del árbol B: "))
        ArbolGlobal = Btree(grado)
        print(f"Grado ingresado: {grado}.")
        print(f"Numero maximo de claves: {ArbolGlobal.max_claves}")
        print(f"Numero minimo de claves: {ArbolGlobal.min_claves}")
        MenuAB.pausar()

    @staticmethod
    def opcion2(): #ABRIR EL MENU DE OPERACIONES
        Menu2()

    @staticmethod
    def opcion3(): #CARGAR ARCHIVO CSV
        MenuAB.cls()
        print("------CARGAR DATOS DESDE ARCHIVO CSV------")
        global ArbolGlobal                                                                                              
        if ArbolGlobal is None:
            print("Primero debes establecer el grado del árbol (opción 1).")
        else:
            ruta="/Users/edwinsoto/Desktop/CSVTarea100.csv"
            ArbolGlobal.archivoCSV(ruta)
        MenuAB.pausar()

    @staticmethod
    def opcion4(): #GENERAR EL GRAFICO EN GRAPHVIZ
        MenuAB.cls()
        print("------GENERAR GRAFICO EN GRAPHVIZ------")
        if ArbolGlobal is not None:
            ArbolGlobal.generar_visualizacion()
        else:
            print("Primero debes establecer el grado del árbol (opción 1).")
        MenuAB.pausar()

    @staticmethod
    def opcion5(): #SALIR DEL PROGRAMA
        MenuAB.cls()
        print("Saliendo del programa...")
        exit()

class MenuOperaciones:
    @staticmethod
    def menu(): #VISION GENERAL DEL  MENU OPERACIONES
        os.system("cls" if os.name == "nt" else "clear")
        print("-----MENU DE OPERACIONES----")
        print("-------------------------------------------:")
        print("1. Inserte claves")
        print("2. Buscar claves")
        print("3. Regresar")

    @staticmethod
    def opcion1(): #AGREGAR NODOS DENTRO DEL ARBOL
        global ArbolGlobal
        MenuAB.cls()
        if ArbolGlobal is None:
            print("Primero debes establecer el grado del árbol B (opción 1).")
            MenuAB.pausar()
            return

        print("-----INGRESAR CLAVES-----")
        while True:
            entrada = input("Ingrese una clave (o escriba 'salir' para terminar): ")
            if entrada.lower() == 'salir':
                break
            if entrada.isdigit():
                clave = int(entrada)
                ArbolGlobal.agregar(clave)
                print(f"Clave {clave} insertada.")
            else:
                print("Entrada no válida. Por favor, ingrese un número o 'salir'.")
        MenuAB.pausar()

    @staticmethod
    def opcion2(): #BUSCAR NODOS DENTRO DEL ARBOL
        MenuAB.cls()
        print("------BUSCAR CLAVE------")
        valor = input("Ingrese la clave que desea buscar en el árbol: ")
        if valor.isdigit():
            numero = int(valor)
            global ArbolGlobal
            encontrado = ArbolGlobal.buscar(numero)
            if encontrado:
                print(f"Nodo {numero} encontrado en el árbol.")
            else:
                print(f"El nodo {numero} no se encuentra en el árbol.")
        else:
            print(f"'{valor}' no es un número válido.")
        MenuAB.pausar()

    @staticmethod
    def opcion3(): #SALIR DEL MENU DE OPERACIONES
        Menu()


#METODO PARA VISUALIZAR MENU PRINCIPAL
def Menu():
    global ArbolGlobal
    while True:
        MenuAB.menuPrincipal()
        seleccion = input("Seleccione una opción (1-5): ")
        if seleccion == '1':
            MenuAB.opcion1()
        elif seleccion == '2':
            if ArbolGlobal is None:
                print("Primero debes establecer el grado del árbol B (opción 1).")
                MenuAB.pausar()
            else:
                MenuAB.opcion2()
        elif seleccion == '3':
            MenuAB.opcion3()
        elif seleccion == '4':
            MenuAB.opcion4()
        elif seleccion == '5':
            MenuAB.opcion5()
        else:
            MenuAB.cls()
            print("Por favor seleccione una opción válida.")
            MenuAB.pausar()

#METODO PARA VISUALIZAR MENU OPERACIONES
def Menu2():
    while True:
        MenuOperaciones.menu()
        seleccion2 = input("Seleccione una opcion (1-3): ")
        if seleccion2 == '1':
            MenuOperaciones.opcion1()
        elif seleccion2 == '2':
            MenuOperaciones.opcion2()
        elif seleccion2 == '3':
            MenuOperaciones.opcion3()
        else:
            MenuAB.cls()
            print("Por favor seleccione una opción válida")
            MenuAB.pausar()

Menu()  # MOSTRAR EL MENU PRINCIPAL EN CONSOLA
