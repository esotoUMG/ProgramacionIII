import os
import graphviz
import csv

# Nodo básico del árbol binario de búsqueda
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

# Árbol binario de búsqueda (ABB)
class ABB:
    def __init__(self):
        self.Raiz = None  # Referencia al nodo raíz

    # Inserta un valor en el árbol de forma recursiva
    def agregar(self, valor, nodo):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self.agregar(valor, nodo.izq)
        elif valor > nodo.valor:
            nodo.der = self.agregar(valor, nodo.der)
        return nodo

    # Busca si un valor existe en el árbol
    def encontrar(self, valor, nodo):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self.encontrar(valor, nodo.izq)
        else:
            return self.encontrar(valor, nodo.der)

    # Encuentra el nodo con el valor menor (útil para eliminar)
    def encontrarmenor(self, nodo):
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    # Elimina un nodo del árbol
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

    # Elimina completamente el árbol
    def eliminarraiz(self):
        self.Raiz = None
        print("El árbol ha sido eliminado.")

    # Genera una visualización del árbol usando Graphviz
    def visualizar(self):
        if not self.Raiz:
            print("El árbol está vacío.")
            return

        dot = graphviz.Digraph('ArbolBinarioBusqueda', format='png')

        # Método recursivo para recorrer y graficar el árbol
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

        ruta_guardado = os.path.expanduser(f"~/Desktop/arbol_binario")
        dot.render(ruta_guardado, format="png")
        print(f'La visualización se ha guardado como {ruta_guardado}.png')

    def archivoCSV(self,nombreArchivo):
        try: 
            with open(nombreArchivo, newline='', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                valores_cargados=0
                for fila in lector:
                    for valor in fila:
                        try:
                            numero = int(valor)
                            self.Raiz = self.agregar(numero, self.Raiz)
                            valores_cargados += 1
                        except ValueError:
                            print(f"Valor inválido en CSV: {valor}. Se omitirá.")

            if valores_cargados > 0:
                print(f"Se han agregador {valores_cargados} valores desde el archivo.csv")
            else:
                print("No se encontraron valores válidos en el archivo.")
        except FileNotFoundError:
            print(f"No se encontró el archivo en {nombreArchivo}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")


# Instancia global del árbol
arbol_global = ABB()

# Menú principal del programa
class MenuABB:
    @staticmethod
    def menuPrincipal():
        os.system("cls" if os.name == "nt" else "clear")
        print("Bienvenido al programa de Arboles\n")
        print("-------------------------------------------:")
        print("Por favor indique que desea hacer:")
        print("-------------------------------------------:")
        print("1) Insertar Nodo")
        print("2) Eliminar Nodo")
        print("3) Buscar Nodo en Arbol")
        print("4) Cargar datos desde un archivo")
        print("5) Eliminar todo el Arbol")
        print("6) Salir")

    @staticmethod
    def pausar():
        input("\nPresiona enter para continuar...")
    @staticmethod
    def cls():
        os.system("cls" if os.name == "nt" else "clear")

    # Inserta nodos uno a uno desde consola hasta que se escriba "salir"
    @staticmethod
    def opcion1():
        os.system("cls" if os.name == "nt" else "clear")
        global arbol_global
        print("------INSERTAR NODO------")
        print("Por favor ingrese el número que desea agregar, para finalizar escriba 'salir': ")
        while True:
            valor = input()
            if valor.lower() == 'salir':
                break
            if valor.isdigit():
                numero = int(valor)
                arbol_global.Raiz = arbol_global.agregar(numero, arbol_global.Raiz)
                print(f"Nodo {numero} agregado correctamente.")
            else:
                print(f"'{valor}' no es un número válido.")
            print("Agregue otro número: ")
        arbol_global.visualizar()

    # Elimina un nodo especificado por el usuario
    @staticmethod
    def opcion2():
        os.system("cls" if os.name == "nt" else "clear")
        print("------ELIMINAR NODO------")
        valor = input("Ingrese el nodo que desea eliminar: ")
        if valor.isdigit():
            numero = int(valor)
            global arbol_global
            arbol_global.Raiz = arbol_global.eliminar(numero, arbol_global.Raiz)
            print(f"Nodo {numero} eliminado correctamente.")
            arbol_global.visualizar()
        else:
            print(f"'{valor}' no es un número válido.")

    # Busca un nodo en el árbol
    @staticmethod
    def opcion3():
        os.system("cls" if os.name == "nt" else "clear")
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

    # Placeholder para cargar desde archivo (pendiente)
    @staticmethod
    def opcion4():
        os.system("cls" if os.name == "nt" else "clear")
        print("------CARGAR DATOS DESDE ARCHIVO------")
        arbol_global.archivoCSV("~/Desktop/CSVTarea100.csv")
        arbol_global.visualizar()
        input("\nPresiona enter para continuar...")

    # Elimina todo el árbol si el usuario lo confirma
    @staticmethod
    def opcion5():
        os.system("cls" if os.name == "nt" else "clear")
        print("------ELIMINAR ÁRBOL------")
        confirmacion = input("¿Desea eliminar el árbol completo? (S/N): ").strip().upper()
        if confirmacion == "S":
            global arbol_global
            arbol_global.eliminarraiz()
        else:
            print("Operación cancelada.")
        arbol_global.visualizar()

    # Finaliza el programa
    @staticmethod
    def opcion6():
        os.system("cls" if os.name == "nt" else "clear")
        print("Saliendo del programa...")
        exit()

# Lógica del menú principal
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
            os.system("cls" if os.name == "nt" else "clear")
            print("Por favor seleccione una opción válida")
            MenuABB.pausar()
            os.system("cls" if os.name == "nt" else "clear")

menu()
