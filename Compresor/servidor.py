import io
import socket
import ssl
from descompresion import descomprimir


def iniciar_servidor(condicion_inicializacion, clave):
    host = 'localhost'
    puerto = 65432

    # Crear un socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, puerto))
    sock.listen(5)

    # Configuración SSL
    contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    contexto.load_cert_chain(certfile="certificado.pem", keyfile="llave_privada.pem")
    
    # Desactivar la verificación del certificado del cliente
    contexto.verify_mode = ssl.CERT_NONE

    print(f"Servidor escuchando en {host}:{puerto}...")

    with condicion_inicializacion:
        condicion_inicializacion.notify()

    conn, addr = sock.accept()
    conn_ssl = contexto.wrap_socket(conn, server_side=True)
    print(f"Conexión establecida desde {addr}")
            
    datos_totales = b""
    while True:
        datos = conn_ssl.recv(1024)
        if not datos:
            break
        datos_totales += datos

    # Aquí debes descifrar y descomprimir los datos
    texto_descomprimido = descomprimir(datos_totales, clave)
    print(f"Datos recibidos y descomprimidos: {texto_descomprimido}")

    conn_ssl.close()
    sock.close()

    