## Generar clave privada para el servidor

Instalar openssl:

´´´
sudo apt update
sudo apt install openssl
´´´

Generar un certificado autofirmado y una llave privada:

´´´
openssl req -x509 -newkey rsa:4096 -keyout llave_privada.pem -out certificado.pem -days 365
´´´

Password:
Hello

clave de cifrado:
