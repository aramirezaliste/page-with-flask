# page-with-flask

## Descripcion

Creando una pagina con flask

## Dependencias 
Incluidas en el requirements.txt
- blinker==1.7.0
- click==8.1.7
- Flask==3.0.1
- itsdangerous==2.1.2
- Jinja2==3.1.3
- MarkupSafe==2.1.4
- Werkzeug==3.0.1

## Como instalar las dependencias
- Crear el entorno virtual en Linux/Mac 
    - `virtualenv env`
- Entrar en el entorno virtual en Linux/Mac 
    - `source env/bin/activate`
- Instalar las dependencias
    - `pip install -r requirements.txt`

## Como Lanzar el servidor interno que viene con Flask
**Solo se debe usar para el desarrollo de la aplicacion**
- Declarar la variable FLASK_APP en el fichero `env/bin/activate` en Linux/Mac
    - Añadir al final del fichero `export FLASK_APP="run.py"`
- Salir del entorno virtual
    - `deactivate`
- Volver a entrar en el entorno virtual, para ver reflejado los cambios en Linux/Mac 
    - `source env/bin/activate`
- Lanzar el servidor de Flask
    - `python3 -m flask run` o `flask run`

### Añadir el modo debug en el servidor interno para desarrollo
**Solo se debe usar para el desarrollo de la aplicacion**
- Añadir la variable de entorno FLASK_ENV y FLASK_DEBUG en el fichero `env/bin/activate` en Linux/Mac
    - Añadir al final del fichero `export FLASK_ENV="development"` y `export FLASK_DEBUG=1`
- Salir del entorno virtual
    - `deactivate`
- Volver a entrar en el entorno virtual, para ver reflejado los cambios en Linux/Mac 
    - `source env/bin/activate`
- Lanzar el servidor de Flask en modo debug
    - `python3 -m flask run` o `flask run`