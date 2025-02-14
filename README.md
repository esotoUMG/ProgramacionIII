# Lista Doblemente Enlazada con Visualización en Graphviz

Este proyecto implementa una **lista doblemente enlazada** en Python con funcionalidades para **insertar, eliminar y visualizar** los nodos de la lista. Además, genera representaciones gráficas de la lista utilizando la biblioteca **Graphviz**, guardando cada visualización en una imagen PNG.

## Características
- Inserción de nodos al inicio o al final de la lista.
- Eliminación de nodos por nombre y apellido.
- Visualización automática de la lista después de cada operación.
- Generación de imágenes en formato PNG mostrando la estructura de la lista.

## Uso
El programa proporciona un menú interactivo en la terminal para realizar operaciones en la lista:

1. **Insertar al principio**: Agrega un nodo al inicio de la lista.
2. **Insertar al final**: Agrega un nodo al final de la lista.
3. **Eliminar por nombre y apellido**: Busca y elimina un nodo específico.
4. **Mostrar lista**: Muestra los elementos actuales de la lista en consola.
5. **Salir**: Finaliza la ejecución del programa.

## Visualización con Graphviz
Cada vez que se realiza una inserción o eliminación, el programa genera automáticamente una imagen mostrando la estructura de la lista.
El grafico se guarda en el escritorio de la computadora

- La imagen se guarda en el escritorio con el nombre **"lista_doble_enlazada.png"**.
- Las conexiones entre nodos reflejan la relación **doblemente enlazada** (siguiente ↔ anterior).

## Ejemplo de Uso
**Entrada en consola:**
```
----Menú----
1. Insertar al principio
2. Insertar al final
3. Eliminar por nombre y apellido
4. Mostrar lista
5. Salir
Seleccione una opción: 1
Ingrese un nombre: Juan
Ingrese un apellido: Pérez
```

## Integrantes y participación
- Edwin Soto 
- Werner Ortiz

