import io
from arbolHuffman import construir_arbol_huffman, construir_tabla_codificacion, obtener_representacion_arbol


def comprimir(texto):
    raiz = construir_arbol_huffman(texto)
    tabla_codificacion = construir_tabla_codificacion(raiz)
    texto_comprimido = "".join([tabla_codificacion[char] for char in texto])
    
    representacion_arbol = obtener_representacion_arbol(raiz)
    longitud_arbol = format(len(representacion_arbol), '016b')
    
    return longitud_arbol + representacion_arbol + texto_comprimido


def comprimir_from_file(file_path):
    with io.open(file_path, 'r', encoding='utf-8') as file:
        texto = file.read()
    
    return comprimir(texto), texto


