# Componente main

El componente main está diseñado para manejar operaciones de compresión y descompresión de archivos, y enviar archivos comprimidos a un receptor a través de una conexión de red.

## Función mostrar_menu

La función `mostrar_menu` imprime un menú interactivo en la consola que le permite al usuario elegir entre tres operaciones:

1. Comprimir un archivo de texto.
2. Descomprimir un archivo previamente comprimido.
3. Enviar un archivo comprimido a un receptor.

La función devuelve la opción seleccionada por el usuario.

## Función main

La función main es el punto de entrada del programa y maneja la lógica principal basada en la selección del usuario:

### Opción Comprimir

- Solicita al usuario que introduzca la ruta del archivo que desea comprimir.
- Verifica si el archivo existe y calcula su tamaño original en bits.
- Comprime el archivo utilizando la función comprimir_from_file importada del módulo compresion.
- Muestra el tamaño del texto comprimido y guarda el resultado con la función guardar_comprimido importada del módulo almacenar.

### Opción Descomprimir

- Solicita al usuario que introduzca la ruta del archivo comprimido para descomprimir y la clave de cifrado.
- Verifica si el archivo existe.
- Descomprime el archivo utilizando la función descomprimir_from_file importada del módulo descompresion.
- Muestra el texto descomprimido.

### Opción Enviar archivo comprimido

- Verifica si existe un archivo denominado com_file.bin.
- Lee el contenido del archivo y solicita al usuario la clave de cifrado.
- Inicia un servidor en un hilo separado utilizando la función iniciar_servidor importada del módulo servidor para esperar y recibir datos.
- El servidor es iniciado con la condición de que solo continúe cuando la condición de inicialización se active, lo cual ocurre una vez que está listo para recibir datos.
- Envía los datos del archivo comprimido a través de la función enviar_datos importada del módulo enviarDatos.

## Threading

El uso de threading permite que el servidor se ejecute de manera concurrente con el resto del programa, esperando en segundo plano a que se cumplan ciertas condiciones antes de proceder con la operación de envío.

## Código Completo

```python
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
```

## Explicación

Explicación por partes de lo que hace el componente main

### Mostrar Menu

Se defíne el menú del usuario

```python
def mostrar_menu(): #Se define el menu del UI
    print(f"###############################")
    print(f"# Compresor de Texto #")
    print(f"###############################\n")
    print("1. Comprimir")
    print("2. Descomprimir")
    print("3. Enviar archivo comprimido a receptor")
    return input("Seleccione una opción (1/2/3): ") #Se pide al usuario un input y se devuelve.
```

### Lógica principal del programa (`main()`)

Se define la lógica principal del programa

```python
def main(): #Se define la función que determina las acciones del programa
  opcion = mostrar_menu() # Se guarda el input de "mostrar_menu" en la variable "opcion"

  # Se defina la estructura condicional
  if opcion == '1': #Si opcion = 1 entonces comprimir
  elif opcion == '2': #Si opcion = 2 entonces descomprimir
  elif opcion == '3': #Si opcion = 3 entonces enviar datos
  else: #Si ninguna opción es verdadera entonces imprimir mensaje de error
    print("Opción no válida.")

if __name__ == "__main__":
  main()

```

Python establece la variable `__name__` para saber si es un script principal, si este es igual a `__main__` entonces se ejecuta como programa principal.

```python
if __name__ == "__main__":
  main() #Si __name__ = __main__ entonces se ejecuta el programa.
```

### Opcion == 1 (Comprimir)

El siguiente código es la lógica de compresión el archivo menu.py

```python
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
```

Si es opción si es la opción "1". Solicitará al usuario la ruta del archivo que se desea comprimir. Posteriormente verificará si existe, si este existe retornará su tamaño en bits. Si no existe mostrará un error handler.

```python
if opcion == '1': #Si opcion = 1 entonces comprimir

  # Solicita al usuario la ruta del archivo que desea comprimir. El resultado se almacena en la variable file_path.
  file_path = input("\nIntroduce la ruta del archivo que deseas comprimir: ")

 # Verifica si la ruta proporcionada por el usuario existe. Si no , ejecuta error handler
  if not os.path.exists(file_path):
  print("Error: La ruta del archivo no es válida.")
  return

 # Se obtiene el tamaño del archivo y se multiplica por 8 para convertirlos a bits.
  size_original = os.path.getsize(file_path) * 8
  print(f"\nTamaño del archivo original: {size_original} bits.")
```

Después de mostrar el tamaño pasará al proceso de comprimir. Se llama a la función "comprir_from_file" y de parámetro se guarda "file_path" Es decir la ruta del archivo.
"comprir_from_file" devuelve el texto comprimido y se almacena en "texto_comprimido"

```python
texto_comprimido = comprimir_from_file(file_path)
```

Luego de comprimir el archivo, se mostrará el tamaño de bits en consola. "texto_comprmido" es una cadena de bits, len() cuenta los caracteres que hay en la cadena"

```python
bits_texto_comprimido = len(texto_comprimido)
print(f"Tamaño del texto comprimido: {bits_texto_comprimido} bits.")
```

Una vez comprimido y mostrado el tamaño en bits en consola, se pasará a el proceso de almacenamiento o guardado. Se llama a la función "guardar_comprimido" con el texto comprimido como argumento. Esta función guarda el texto comprimido y devuelve una clave que se utiliza para el cifrado. La clave se almacena en la variable clave.

```python
clave = guardar_comprimido(texto_comprimido)
```

## Opción == 2 (Descomprimir)

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```
