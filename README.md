Este proyecto es un ejemplo básico de cómo utilizar Selenium en PyCharm para automatizar pruebas en una página web. 
En este caso, se ha utilizado la página de demostración "Sauce Labs" 
(https://www.saucedemo.com/).

Configuración del entorno:

Para poder ejecutar este proyecto, es necesario instalar Python 3 y las siguientes bibliotecas:

selenium

pytest

Además, se debe descargar el driver del navegador correspondiente y agregarlo al PATH del sistema. En este proyecto se 
ha utilizado el driver para Chrome, que se puede descargar desde la siguiente página: 
https://sites.google.com/a/chromium.org/chromedriver/downloads

Estructura del proyecto:

/pages: contiene las clases que representan cada una de las páginas de la aplicación.

/tests: contiene los casos de prueba.

/drivers: contiene el driver del navegador.

Ejecución de las pruebas
Para ejecutar las pruebas, basta con abrir una terminal en la carpeta raíz del proyecto y 
ejecutar el siguiente comando:

pytest

Esto ejecutará todos los casos de prueba del proyecto.
