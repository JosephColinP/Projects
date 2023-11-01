import socket
import ssl
from compresion import comprimir



def enviar_datos(datos_cifrados):
    host = 'localhost'
    puerto = 65432

    # Crear un socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Envolver el socket con una capa de seguridad SSL
    contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    
    # Desactivar la verificación del certificado y el nombre del host
    contexto.check_hostname = False
    contexto.verify_mode = ssl.CERT_NONE
    # contexto.load_verify_locations(cafile="url_al_certificado.pem")


    conn_ssl = contexto.wrap_socket(sock, server_hostname=host)
    conn_ssl.connect((host, puerto))

    # Enviar datos
    conn_ssl.sendall(datos_cifrados)  

    conn_ssl.close()

if __name__ == "__main__":
    enviar_datos()

