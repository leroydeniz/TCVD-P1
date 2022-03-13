# Práctica 1 - Web Scraping
Tipología y Ciclo de Vida de los Datos<br/>
Máster en Ciencia de Datos<br/>
Universitat Oberta de Catalunya <br/>

<!-- Tabla de contenidos -->
<details>
  <summary>Indice</summary>
  <ol>
    <li>
      <a href="#Descripción">Descripción</a>      
    </li>
    <li>
      <a href="#Miembros-del-equipo">Miembros del equipo</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Ficheros-del-código-fuente">Ficheros del código fuente</a></li>
    <li><a href="#Recursos">Recursos</a></li>
    <li><a href="#Librerias">Librerias</a></li>
    <li><a href="#Ejecución">Ejecución</a></li>
    <li><a href="#Licencia">Licencia</a></li>
  </ol>
</details>

## Descripción
Con esta práctica se pretende aplicar técnicas de web scraping mediante el lenguaje de programación [Python](https://www.python.org/) para extraer así la información de los proyectos de investigación estudiantil de la Universidad de la República, principal institución educativa de alto nivel en Uruguay concentrando el 90% de la población universitaria.

## Miembros del equipo
Leroy Deniz Pedreira <br/>
David Muñoz Bertrán

## Ficheros del código fuente
El proyecto se estructura de la siguiente manera: <br/>
**TCVD-P1/:** Raíz principal del proyecto <br/>
**TCVD-P1/img/:** Directorio donde se almacenan las imágenes de cada uno de los proyectos, si la contienen <br/>
**TCVD-P1/output/:** Directorio donde se almacena el resultado final del proyecto <br/>
**TCVD-P1/output/paies.csv:** Fichero resultante .csv que contiene toda la información obtenida del scraping <br/>
**TCVD-P1/app.py:** Contiene las intrucciones necesarias para la recolección de datos <br/>
**TCVD-P1/utils.py:** Contiene las funciones reiterativas necesarias y accesibles desde app.py

## Recursos
• Bianco, M., & Sutz, J. (2014). Veinte años de políticas de investigación en la Universidad de la
República. Aciertos, dudas y aprendizajes (junio de 2014). TRILCE. Recuperado 13 de marzo de
2022, de https://www.csic.edu.uy/sites/csic/files/libro_veinte_anos_de_politicas_de_investigacion_en_la_universidad_de_la_republica.pdf <br/>
• Creative Commons. (s. f.). Reconocimiento-CompartirIgual 4.0 Internacional (CC BY-SA 4.0).
Recuperado 13 de marzo de 2022, de https://creativecommons.org/licenses/by-sa/4.0/deed.es_ES <br/>
• García Nieto, J. (2018, septiembre 15). Licencias Creative Commons explicadas para dummies
[Blog]. GENBETA. https://www.genbeta.com/herramientas/licencias-creative-commonsexplicadas-para-dummies <br/>
• Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the
Data.<br/>
• Masip, D. El lenguaje Python. Editorial UOC.</br>
• Simon Munzert, Christian Rubba, Peter Meißner, Dominic Nyhuis. (2015). Automated Data
Collection with R: A Practical Guide to Web Scraping and Text Mining. John Wiley & Sons. <br/>
• Subirats, L., Calvo, M. (2018). Web Scraping. Editorial UOC.<br/>
• Tutorial de Github https://guides.github.com/activities/hello-world.

## Librerias
El script hace uso de las siguientes librerias:

 * random
  ```sh
  import random
  ```
 * requests
  ```sh
  import requests
  ```
 * pandas
  ```sh
  import pandas as pd
  ```
 * BeautifulSoup
  ```sh
  from bs4 import BeautifulSoup
  ```
 * time
 * os.path

## Ejecución
gem install github-markup
