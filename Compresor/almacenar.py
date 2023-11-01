from cifrar import generar_cifrador

def guardar_comprimido(texto_comprimido):
    cifrador, clave = generar_cifrador()

    num_bytes = (len(texto_comprimido) + 7) // 8
    bytes_comprimidos = int(texto_comprimido, 2).to_bytes(num_bytes, byteorder='big')

    texto_cifrado = cifrador.encrypt(bytes_comprimidos)

    with open('com_file.bin', 'wb') as file:
        file.write(texto_cifrado)

    print("\nTexto comprimido y cifrado guardado en 'compressed_file.bin'")
    print(f"Clave de cifrado: {clave.decode()}")

    return clave