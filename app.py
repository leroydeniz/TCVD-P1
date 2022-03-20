import random
import requests # para manejar las urls
import pandas as pd # para manejo de dataframes
from bs4 import BeautifulSoup
from utils import *
import time
from tqdm import tqdm

# Años donde buscar la información, 2010 se excluye por falta de datos
years = [2008, 2009, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

# DataFrame en pandas a rellenar
df = pd.DataFrame(columns = ['Title', 'Link', 'Description', 'Image', 'Year', 'Published'])

# Enlaces a todos los proyectos donde recuperar la información
projects = []

# Procesa año a año
print(f" > Processing editions by year")

for year in tqdm(years):

    # Hará variar el tiempo de respuesta
    t0 = time.time()
      
    try:
        # A través de f-strings parametrizar la consulta para tomar cada una de las ediciones de los proyectos
        page = requests.get(f'https://www.estudiantes.csic.edu.uy/category/proyectos-aprobados/proyectos-{year}/', headers = {'User-Agent': get_header()})
    except requests.exceptions.Timeout:
        # Si cae el servidor o se demora, intenta con el siguiente
        pass

    # Mide el tiempo de respuesta
    response_delay = time.time() - t0
    
    # Demora la siguiente llamada 10 veces el tiempo de respuesta inicial
    time.sleep(4 * response_delay)

    # Obtener la información de cada url a visitar para tomar los datos
    soup = BeautifulSoup(page.content, "html.parser")

    try:
        # Obtiene todos los títulos h2 que contienen los enlaces
        for tmp in soup.find_all('h2'):

            # Toma los enlaces propiamente
            tmp = tmp.a['href']

            # Los añade a la lista de enlaces a proyectos que necesita
            projects.append([tmp,year])
    except Exception as e:
        print(e)
        pass
    
# Indica el número de proyecto que está evaluando
count = 0

# Rascar la información de cada uno de los proyectos partiendo del enlace
print(f" > Processing projects")
for project in tqdm(projects):
    
    # Hará variar el tiempo de respuesta
    t0 = time.time()
    page = requests.get(project[0], headers = {'User-Agent': get_header()})

    # Mide el tiempo de respuesta
    response_delay = time.time() - t0
    
    # Demora la siguiente llamada 10 veces el tiempo de respuesta inicial
    time.sleep(6 * response_delay)

    soup = BeautifulSoup(page.content, "html.parser")

    # Verifica que los campos tengan contenido, sino los pone a None
    try:
        p_title = soup.h1.string.strip()
    except Exception as e:
        p_title = None
        
    try:
        p_description = soup.div(class_='post-content')[0].p.getText().strip()
    except Exception as e:
        p_description = None
        
    try:
        image_path = soup.div(class_='post-content')[0].p.a['href'].strip()
        p_image = load_requests(image_path, count).strip()
    except Exception as e:
        p_image = None
        
    try:
        p_pub_date = soup.find('span', {'class': 'updated'}).text
    except Exception as e:
        p_pub_date = None

    # Sustituir las commas por otro símbolo para facilitar la lectura del
    #df = df.applymap(lambda x: x.replace(',', ''))
    # Añadir la nueva fila al dataframe
    df = df.append({'Title': p_title, 'Link': project[0], 'Description': p_description, 'Image': p_image, 'Year': project[1], 'Published': p_pub_date}, ignore_index=True)

    count += 1

# Crea el fichero CSV en el directorio output-
df.to_csv('output/paies.csv', na_rep='N/A')
print(df)