## FC_APIJugadores

Esta API se desarrolló, se probó, se documento y se publicó principalmente con los siguientes lenguajes y herramientas (algunas otras se especifican en el archivo requirements.txt):

- Python-3.9.2
- FastAPI
- Swagger
- Heroku
- uvicorn
- pytest
- requests
- pydantic

## Demo
[Link a la versión en Heroku Resuelve FC API](https://fcresuelve.herokuapp.com/docs)

*Para probar el endpoit `/jugadores/` ingresa el JSON con la siguiente estructura:

            {
               "jugadores" : [  
                  {  
                     "nombre":"Juan Perez",
                     "nivel":"C",
                     "goles":10,
                     "sueldo":50000,
                     "bono":25000,
                     "sueldo_completo":null,
                     "equipo":"rojo"
                  },
                  {  
                     "nombre":"EL Cuauh",
                     "nivel":"Cuauh",
                     "goles":30,
                     "sueldo":100000,
                     "bono":30000,
                     "sueldo_completo":null,
                     "equipo":"azul"
                  },
                  {  
                     "nombre":"Cosme Fulanito",
                     "nivel":"A",
                     "goles":7,
                     "sueldo":20000,
                     "bono":10000,
                     "sueldo_completo":null,
                     "equipo":"azul"

                  },
                  {  
                     "nombre":"El Rulo",
                     "nivel":"B",
                     "goles":9,
                     "sueldo":30000,
                     "bono":15000,
                     "sueldo_completo":null,
                     "equipo":"rojo"

                  }
               ]
            }

### Getting Started
Para implementar de manera local la aplicación sigue los siguientes pasos:

### Setup

    # Clona el repositorio con la siguiente URL
    $ git clone https://github.com/lnetza/FC_APIJugadores.git
  
    # entra a la carpeta FC_APIJugadores
    $ cd FC_APIJugadores
            
### Instalación

Si ya te encuentras dentro de la carptea `FC_APIJugadores` crea un entorno virtual,  
instalando `virtualenv` con el siguiente comando: `pip install virtualenv`

Dentro de la carpeta `FC_APIJugadores` crea un nuevo entorno virtual ejecutando: `python -m venv env`  

Una vez creado el entorno; procede a activarlo ingresando a la carpeta `FC_APIJugadores/server/env/Scripts` y ejecuta el comando:
   `$ activate`

Ahora regresa a la carpeta `FC_APIJugadores/server` para instalar dependencias necesarias, ejecutando:
  `$ pip install -r requirements.txt`

### Información de Uso

Escribir el siguiente comando par ejecutar la aplicación, dentro de la carpeta `FC_APIJugadores/server`  
    
Ejecuta el siguiente comando:
  `$ uvicorn main:app --reload`
    
            
E ingresa a la siguiente URL para empezar a utilizar la aplicación: http://127.0.0.1:8000/docs


### Ejecutar Pruebas

Este proyecto tiene un test referente al enpoint `/jugadores/`, ejecuta `pytest` dentro de la carpeta `FC_APIJugadores/server`

    $ pytest


