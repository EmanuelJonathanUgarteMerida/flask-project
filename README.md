# Usando Flask

Primera versión de práctica con flask

- instalación: pip install flask , usar en terminal flask para ver las opciones
- definir aplicación principal: set FLASK_APP=hello
- definir el entorno: set FLASK_ENV=development
- para no definir siempre FLASK_APP y FLASK_ENV, usaremos python dotEnv (pip install python-dotenv), creamos los archivos .env-template y .env, .env es donde el servidor va buscar las variables de entorno, por default buscará un archivo .env
- lanzar flash : flask run