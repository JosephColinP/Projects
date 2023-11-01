from cryptography.fernet import Fernet

def generar_cifrador():
    clave = Fernet.generate_key()
    return Fernet(clave), clave

def cifrar_texto(cifrador, texto):
    return cifrador.encrypt(texto.encode())

def descifrar_texto(cifrador, texto_cifrado):
    return cifrador.decrypt(texto_cifrado).decode()