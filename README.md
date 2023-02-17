# CHR

### Iniciar Proyecto:
* `Descargar repositorio`
* `Crear entorno virtual de python`: python -m venv venv
* `Activar entorno virtual e instalar requerimientos con`: pip install -r requirements.txt
* `Crear archivo .env en la carpeta inicial del proyecto django "core" con los siguiente`: 
    [![env.png](https://i.postimg.cc/44vhv5vT/env.png)](https://postimg.cc/w3vvgDbW)
    #### Django settings
    DEBUG=1
    SECRET_KEY=django-insecure-v)joq#9ka7p_5i525@y+ufi2_u$439a$^o&1_vay!^kbemx#_j
    DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

    #### Database settings
    DB_NAME=chr_database
    DB_PASSWORD=Your_postgres_password
    DB_USER=Your_postgres_user
    DB_PORT=5432
    DB_ENGINE=django.db.backends.postgresql_psycopg2
    DB_HOST=localhost
* `Crear la Base de datos en PostgreSQL con el mismo nombre de DB_NAME en el archivo .env e ingresando con el usuario de DB_USER y DB_PASSWORD del .env`
* `ejecutar los comandos de Django`:
    *   python manage.py makemigrations
    *   python manage.py migrate
    *   python manage.py createsuperuser
    *   python manage.py runserver

### Agregar Chrome webdriver para selenium:
* `Agregar el webdriver de chrome en el directorio de la aplicacion django /webscraping/selenium: 
    [![selenium.png](https://i.postimg.cc/vHQx0VXx/selenium.png)](https://postimg.cc/F1BKR1Mh)