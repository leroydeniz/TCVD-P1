# Fichero con utilidades

import requests
import os.path
import random


# Función para obtener la imagen de una URL
def load_requests(source_url):
    r = requests.get(source_url, stream = True)
    if r.status_code == 200:
        aSplit = source_url.split('/')
        if verify_extension(aSplit[len(aSplit)-1]):
            ruta = "img/"+aSplit[len(aSplit)-1]
            output = open(ruta,"wb")
            for chunk in r:
                output.write(chunk)
            output.close()
            return ruta
    return None


# Función para verificar la extensión de la imagen
def verify_extension(name):
    _, extension = os.path.splitext(name)
    if extension in ['.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif']:
        return True
    return False


# Función para hacer variar las cabeceras de las peticiones HTTP
def get_header():
    # Definir cabeceras para envío de petición HTTP
    headers_options = ['Mozilla/5.0', 'Chrome/42.0.2311.135', 'Safari/537.36', 'Edge/12.246', 'AppleWebKit/537.36']

    # Elige un tipo de cabecera aleatoria por llamada
    i = random.choice(headers_options)

    return i