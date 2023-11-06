import heapq
from collections import Counter
from cryptography.fernet import Fernet
from nodo import Nodo

def construir_arbol_huffman(texto):
    frecuencia = Counter(texto)
    cola = [Nodo(char, freq) for char, freq in frecuencia.items()]
    heapq.heapify(cola)

    while len(cola) > 1:
        izq = heapq.heappop(cola)
        der = heapq.heappop(cola)
        nodo_intermedio = Nodo(None, izq.freq + der.freq)
        nodo_intermedio.izquierda = izq
        nodo_intermedio.derecha = der
        heapq.heappush(cola, nodo_intermedio)

    return cola[0]

def construir_tabla_codificacion(raiz, codigo_bin="", tabla={}):
    if raiz is None:
        return 

    if raiz.char is not None:
        tabla[raiz.char] = codigo_bin

    construir_tabla_codificacion(raiz.izquierda, codigo_bin + "0", tabla)
    construir_tabla_codificacion(raiz.derecha, codigo_bin + "1", tabla)

    return tabla

def obtener_representacion_arbol(raiz):
    if raiz is None:
        return ""

    if  raiz.char:
        return "1" + format(ord(raiz.char), '08b') 
    else:
        return "0" + obtener_representacion_arbol(raiz.izquierda) + obtener_representacion_arbol(raiz.derecha)