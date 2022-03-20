# Fichero con utilidades

import requests
import os.path
import random




# Función para obtener la imagen de una URL
def load_requests(source_url, id):
    r = requests.get(source_url, stream = True)
    if r.status_code == 200:

        # Separar la urle /: ['http:', '', 'www.estudiantes.csic.edu.uy', 'wp-content', 'uploads', '2015', '09', '32114scr_654aa682ea813a1195.jpg']
        aSplit = source_url.split('/')

        # Tomar el nombre del fichero 
        filename = aSplit[len(aSplit)-1]

        _, ext = os.path.splitext(filename)
        if verify_extension(ext):

            # Separar el nombre del fichero de imagen: ['32114scr_654aa682ea813a1195', 'jpg']
            ruta = f"img/{id}{ext}"
            output = open(ruta,"wb")
            for chunk in r:
                output.write(chunk)
            output.close()
            return ruta
    return None


# Función para verificar la extensión de la imagen
def verify_extension(ext):
    if ext in ['.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif']:
        return True
    return False


# Función para hacer variar las cabeceras de las peticiones HTTP
def get_header():
    # Definir cabeceras para envío de petición HTTP
    headers_options = ['Mozilla/5.0', 'Chrome/42.0.2311.135', 'Safari/537.36', 'Edge/12.246', 'AppleWebKit/537.36']

    # Elige un tipo de cabecera aleatoria por llamada
    return random.choice(headers_options)