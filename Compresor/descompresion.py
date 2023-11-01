from nodo import Nodo
from cryptography.fernet import Fernet


def reconstruir_arbol(bits):
    tipo_nodo = bits.pop(0)
    
    if tipo_nodo == '1':
        char = chr(int(''.join(bits.pop(0) for _ in range(8)), 2))
        return Nodo(char, None)

    # Nodo intermedio
    nodo = Nodo(None, None)
    nodo.izquierda = reconstruir_arbol(bits)
    nodo.derecha = reconstruir_arbol(bits)
    return nodo



def decodificar(texto_comprimido, arbol):
    nodo_actual = arbol
    resultado = []

    for bit in texto_comprimido:
        if bit == '0':
            nodo_actual = nodo_actual.izquierda
        else:  # bit == '1'
            nodo_actual = nodo_actual.derecha

        if nodo_actual.char is not None:
            resultado.append(nodo_actual.char)
            nodo_actual = arbol 

    return ''.join(resultado)


def cargar_cifrador(clave):
    return Fernet(clave)

def descifrar_texto(cifrador, texto_cifrado):
    return cifrador.decrypt(texto_cifrado).decode()

def descomprimir(datos, clave):
    cifrador = cargar_cifrador(clave)
    bytes_descifrados = cifrador.decrypt(datos)

    bits = ''.join(bin(byte)[2:].zfill(8) for byte in bytes_descifrados)
    
    longitud_arbol = int(bits[:16], 2)
    bits_arbol = bits[16:16+longitud_arbol]
    bits_texto = bits[16+longitud_arbol:]
    
    arbol = reconstruir_arbol(list(bits_arbol))
    texto_original = decodificar(bits_texto, arbol)
    
    return texto_original



def descomprimir_from_file(file_path, clave):
    cifrador = cargar_cifrador(clave)

    with open(file_path, 'rb') as file:
        texto_cifrado = file.read()
        bytes_descifrados = cifrador.decrypt(texto_cifrado)

    bits = ''.join(bin(byte)[2:].zfill(8) for byte in bytes_descifrados)
    
    longitud_arbol = int(bits[:16], 2)
    bits_arbol = bits[16:16+longitud_arbol]
    bits_texto = bits[16+longitud_arbol:]
    
    arbol = reconstruir_arbol(list(bits_arbol))
    texto_original = decodificar(bits_texto, arbol)
    
    return texto_original



