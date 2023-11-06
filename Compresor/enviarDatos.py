import socket
import ssl
from compresion import comprimir



def enviar_datos(datos_cifrados):
    host = 'localhost'
    puerto = 65432
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    contexto.check_hostname = False
    contexto.verify_mode = ssl.CERT_NONE
    conn_ssl = contexto.wrap_socket(sock, server_hostname=host)
    conn_ssl.connect((host, puerto))
    conn_ssl.sendall(datos_cifrados)  
    conn_ssl.close()

if __name__ == "__main__":
    enviar_datos()

