# Proyecto de elementos

Este proyecto tiene como objetivo desarrollar un sistema en python que guarde bulks en la base de datos,
con su respectivo parameters y también un servicio que retorne los bulk dependiendo su estado en la base de datos


# Instalacion del proyecto

1. Crear un entorno virtual

2. Correr el comando para instalar todos los requerimientos que se necesitan
````commandline
pip install -r requirements\requirements.txt
````
3. Crear la imagen del contenedor
````commandline
docker compose build
````
4. Subir la imagen para crear el contenedor respectivo
````commandline
docker compose up
````

# Ejecucion de tests

````commandline
docker compose run --rm --entrypoint=pytest worker tests/    
````

# Visualizacion swagger

Para visualizar la documentacion de los servicios expuestos seria

````url
http://127.0.0.1:5000/apidocs
````


## Objetivo del Proyecto

El objetivo principal de este proyecto es crear un sistema Python que se conecte a una base de datos de propiedades, recopile datos relevantes y los procese según los requisitos específicos del usuario. Esto puede incluir la extracción de información, la generación de informes o la realización de análisis de datos.

## Plan de Desarrollo

El desarrollo de este proyecto seguirá un enfoque iterativo y se organizará en las siguientes etapas:

1. **Definición de Requisitos**: Se recopilarán y documentarán los requisitos del proyecto, incluyendo los tipos de datos que se deben extraer y procesar, y los resultados esperados.

2. **Diseño de la Arquitectura**: Se diseñará la arquitectura general del sistema, incluyendo la estructura de directorios, la interacción con la base de datos y el flujo de procesamiento de datos.

3. **Implementación**: Se desarrollarán los componentes del sistema utilizando las bibliotecas mencionadas y siguiendo las mejores prácticas de codificación. Se realizarán pruebas unitarias para garantizar la calidad del código.

4. **Pruebas y Validación**: Se realizarán pruebas exhaustivas para asegurarse de que el sistema funcione correctamente y cumpla con los requisitos definidos.

5. **Documentación**: Se elaborará una documentación completa que incluya instrucciones de instalación, uso y mantenimiento del sistema.
