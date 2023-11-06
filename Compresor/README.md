# Comresor de archivos

Este es un compresor de texto con cifrado, el programa toma archivos de texto (.txt), los comprime usando la codificación de Huffman y luego cifra el contenido comprimido antes de guardarlo como un archivo binario (.bin). También puede descomprimir y descifrar archivos que previamente ha procesado.

## ¿Cómo Está Contruido?

Interfaz de Usuario (main.py): Un menú interactivo que guía al usuario a través de las opciones para comprimir, descomprimir y enviar archivos.

Compresión (compresion.py): Funciones que implementan el algoritmo de Huffman para convertir el texto normal en un formato comprimido representando caracteres comunes con códigos más cortos.

Cifrado (almacenar.py y cifrar.py): Utilizan la librería cryptography para cifrar el texto comprimido con una clave generada que es necesaria para el descifrado posterior.

Descompresión (descompresion.py): Funciones para revertir el proceso de compresión, recuperando el texto original a partir de su versión comprimida.

Comunicación en Red (servidor.py y enviarDatos.py): Permiten enviar y recibir datos a través de una conexión SSL/TLS segura.

## ¿Cómo de utiliza?

1. Iniciar el Programa: Ejecutar main.py e introducir la opción deseada en el menú: comprimir, descomprimir o enviar archivo.

Linux command:

´´´
./main.py
´´´

2. Comprimir: Proporcionar la ruta del archivo .txt a comprimir. El programa mostrará el tamaño del archivo original y del archivo comprimido y cifrado, generando una clave para su cifrado.

Linux command:

´´´
ruta/del/archivo/.txt
´´´

Descomprimir: Indicar la ruta del archivo .bin y proporcionar la clave de cifrado correspondiente para obtener el texto original.

Linux command:

´´´
ruta/del/archivo/.txt
´´´

Enviar Archivo: El archivo comprimido y cifrado se envía a un receptor a través de una conexión de red segura. Es necesario ejecutar un servidor que escuche las conexiones entrantes para recibir el archivo.

Linux command:

´´´
clave-del-cifrado
´´´

Linux command:
´´´
clave-del-servidor
´´´

## Generar clave privada para el servidor

Instalar openssl:

´´´
sudo apt update
sudo apt install openssl
´´´

### Generar un certificado autofirmado y una llave privada:

´´´
openssl req -x509 -newkey rsa:4096 -keyout llave_privada.pem -out certificado.pem -days 365
´´´

Contraeña actual:
Hello

## Guía del programa

Para obtener una explicación detallada del programa, visite el [Menú Principal de la Guía](Guia/menu_principal.md).
