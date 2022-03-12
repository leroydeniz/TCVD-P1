import requests # para manejar las urls
import pandas as pd # para manejo de dataframes
from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep
headers = {'User-Agent': 'Mozilla/5.0'}

# Años donde buscar la información, 2010 se excluye por falta de datos
years = [2008, 2009, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

# DataFrame en pandas a rellenar
df = pd.DataFrame(columns = ['Title', 'Link', 'Description', 'Image', 'Service', 'Year'])

# Enlaces a todos los proyectos donde recuperar la información
projects = []

# Procesa año a año
for year in years:
    print(f"Processing: {year}")
    
    # A través de f-strings parametrizar la consulta para tomar cada una de las ediciones de los proyectos
    page = requests.get(f'https://www.estudiantes.csic.edu.uy/category/proyectos-aprobados/proyectos-{year}/', headers = headers)

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

# Cantidad de proyectos
number_of_projects = len(projects)
print(number_of_projects)

'''# Rascar la información de cada uno de los proyectos partiendo del enlace
for project in projects:
    print(f"Processing: {project}")
    page = requests.get(project, headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")

    p_title = soup.h1.content

    # Añadir la nueva fila al dataframe
    df = df.append({'Title': p_title, 'Link': project, 'Description': p_description, 'Image': p_image, 'Service': p_service, 'Year': p_year})

print(df)'''

'''# Barra de avance de proceso
for i in tqdm(range(0, 100), total = 100, desc ="Processing"):
    sleep(.1)'''