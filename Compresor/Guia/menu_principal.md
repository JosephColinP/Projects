# Documentación del Compresor y Cifrador de Archivos

Este programa es una herramienta de compresión y cifrado de archivos de texto. Utiliza el algoritmo de Huffman para la compresión y la biblioteca `cryptography` para el cifrado. Está diseñado para permitir a los usuarios comprimir archivos de texto, descomprimir archivos de texto comprimidos y cifrados, y enviar archivos comprimidos y cifrados a un receptor a través de una conexión segura.

## Índice de Componentes

A continuación, se encuentra el índice de los componentes con su correspondiente documentación:

- [main](./main.md)
- [nodo](./nodo.md)
- [arbolHuffman](./arbolHuffman.md)
- [compresion](./compresion.md)
- [cifrar](./cifrar.md)
- [almacenar](./almacenar.md)
- [descompresion](./descompresion.md)
- [enviarDatos](./enviarDatos.md)
- [servidor](./servidor.md)

Cada uno de estos archivos de documentación contiene información detallada sobre su componente específico, ejemplos de uso, y cualquier dependencia necesaria para que el componente funcione correctamente dentro del programa.

## Uso del Programa

El programa se ejecuta desde la línea de comandos y ofrece un menú interactivo con las siguientes opciones:

1. **Comprimir:** Permite al usuario seleccionar un archivo de texto para comprimirlo.
2. **Descomprimir:** Permite al usuario seleccionar un archivo comprimido y cifrado para descomprimirlo ingresando la clave correspondiente.
3. **Enviar archivo comprimido a receptor:** Inicia un servidor y envía el archivo comprimido y cifrado a un receptor especificado.

Para comenzar a utilizar el programa, se debe ejecutar el script `main.py` con Python3 y seguir las instrucciones en el menú.

```bash
./main.py
```
