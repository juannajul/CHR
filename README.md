# CHR

### Iniciar Proyecto:
* `Descargar repositorio`
* `Crear entorno virtual de python`: python -m venv venv
* `Activar entorno virtual e instalar requerimientos con`: pip install -r requirements.txt
* `Crear archivo .env en la carpeta inicial del proyecto django "core" con los siguiente`: 
    [![env.png](https://i.postimg.cc/44vhv5vT/env.png)](https://postimg.cc/w3vvgDbW)
    [![env2.png](https://i.postimg.cc/RhdMqG37/env2.png)](https://postimg.cc/jnWVFH42)
    
    # Django Settings
    Django settings
    DEBUG=1
    SECRET_KEY=django-insecure-v)joq#9ka7p_5i525@y+ufi2_u$439a$^o&1_vay!^kbemx#_j
    DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

    # Database settings
    DB_NAME=chr_database
    DB_PASSWORD=Your_postgres_password
    DB_USER=Your_postgres_user
    DB_PORT=5432
    DB_ENGINE=django.db.backends.postgresql_psycopg2
    DB_HOST=localhost

* `Crear la Base de datos en PostgreSQL con el mismo nombre de DB_NAME en el archivo .env e ingresando con el usuario de DB_USER y DB_PASSWORD del .env`

### Agregar Chrome webdriver para selenium:
* `Agregar el webdriver de chrome en el directorio de la aplicación django /webscraping/selenium`: 
    [![selenium.png](https://i.postimg.cc/vHQx0VXx/selenium.png)](https://postimg.cc/F1BKR1Mh)

    
* `ejecutar los comandos de Django`:
    *   python manage.py makemigrations
    *   python manage.py migrate
    *   python manage.py createsuperuser
    *   python manage.py runserver

### Descripcion de las Tareas:

#### Tarea 1:
* Para la "tarea 1" se creó la aplicación de django citybike con sus urls, models y views.
* Al ingresar a la ruta: 127.0.0.1:8000/citybike/get_citybike_network_info/ :
    * Obtendra toda la informacion de la API mediante la librería requests.
    * La informacion se guardaran en los modelos creados en la base de datos.
    * retornará un JSONresponse con la informacion obtenida de la API.
    * La infomracion se puede observar ademas iniciando sesión en el django admin.
    * el modulo "create_networks" se encarga de guardar toda la información obtenida de la API en la base de datos.

#### Tarea 2:
* Al realizar la "tarea 2" se creó la aplcación de django webscraping cons sus urls, models y views.
* al ingresar en la ruta: http://127.0.0.1:8000/scraping/get_environmental_info/ :
    * La aplicación obtendrá la información proporcionada por la tabla de la url: https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php navegando utilizando selenium.
    * Utilizando selenium navegará a través de todas las paginas de la tabla de dicha url.
    * Guardará toda la información obtenida de la pagina en la base de datos a traves de su modelo Project.
    * Creará un archivo json en la siguiente ruta: mediafiles/projects_json/projects.json [![json.png](https://i.postimg.cc/J4hrTH4R/json.png)](https://postimg.cc/6TDxq3vP)
    * el modulo selenium en la app webscraping (webscraping/selenium/) se encarga de obtener toda la información de la url porporcionada, 
    guardarla en la base de datos y crear el archivo json.
    * Todos los datos pueden ser observados en el modelo Project dentro del Django admin.
