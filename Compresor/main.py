#!/usr/bin/env python3
import os
import threading
from compresion import comprimir_from_file
from almacenar import guardar_comprimido
from descompresion import descomprimir_from_file
from enviarDatos import enviar_datos
from servidor import iniciar_servidor

condicion_inicializacion = threading.Condition()

def mostrar_menu(): 
    print(f"###############################")
    print(f"# Compresor de Texto #")
    print(f"###############################\n")
    print("1. Comprimir")
    print("2. Descomprimir")
    print("3. Enviar archivo comprimido a receptor")
    return input("Seleccione una opción (1/2/3): ")

def main():
    opcion = mostrar_menu()
    
    if opcion == '1': 
        file_path = input("\nIntroduce la ruta del archivo que deseas comprimir: ")
        if not os.path.exists(file_path):
            print("Error: La ruta del archivo no es válida.")
            return
        size_original = os.path.getsize(file_path) * 8
        print(f"\nTamaño del archivo original: {size_original} bits.")
        texto_comprimido = comprimir_from_file(file_path)
        bits_texto_comprimido = len(texto_comprimido)
        print(f"Tamaño del texto comprimido: {bits_texto_comprimido} bits.")
        clave = guardar_comprimido(texto_comprimido)
       
    elif opcion == '2': 
        file_path = input("\nIntroduce la ruta del archivo comprimido que deseas descomprimir: ")
        if not os.path.exists(file_path):
            print("Error: La ruta del archivo no es válida.")
            return
        clave = input("\nIntroduce la clave de cifrado: ").encode()
        texto_descomprimido = descomprimir_from_file(file_path, clave)
        print(f"Texto descomprimido: {texto_descomprimido}")

    elif opcion == '3': 
        file_path = 'com_file.bin'
        if not os.path.exists(file_path):
            print("Error: El archivo comprimido no existe.")
            return
        with open(file_path, 'rb') as file:
            datos = file.read()
        clave = input("\nIntroduce la clave de cifrado para descifrar los datos recibidos: ").encode()
        
        threading.Thread(target=iniciar_servidor, args=(condicion_inicializacion, clave)).start()
        
        with condicion_inicializacion:
            condicion_inicializacion.wait()

        enviar_datos(datos)
        exit()

    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main() 