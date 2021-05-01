# Newsletter API DRF
API para la creación de boletines, así como de su visualización.
con 3 forma de uso:
1. cliente: Puede ver los boletines pero no puede editar nada
2. user: Puede darle like a los boletines que mas le gustan y suscribirse a los que tiene un mínimo de votos.
3. Admin: puede crear boletines y puede invitar o ser invitado para editar otros boletines

## Requisitos
Python 3.8 & 
PIP

## Instalación
Descarge o clone el repositorio, si decidió el método por descarga también deberá
descomprimir el proyecto.

Abre un consola que apunte al proyecto y realiza lo siguiente.
- Crear entorno virtual ***`python3 -m venv env`***

- Activar entorno virtual 
	* Unix y Mac ***`env\Scripts\activate.bat`***
	* Windows ***`env/bin/activate`***

- Instalar dependencias
	* ***`python -m pip install -r requirements.txt***
	
- variables de entorno
	* crea un archivo `.env` para las varibles de entorno en la carpeta Newsletter con los siguiente campos
		1. `SECRET_KEY= tu_clave_secreta`
		2. `ALLOWED_HOSTS= Hots_que permites ej. 127.0.0.1`
		3. `DEBUG= Ture/False`
		
- Aplicar migraciones


    	python manage.py makemigrations
    	python manage.py migrate
    	python manage.py runserver

> Puedes detener el servidor con ctr + c

- crea un superusuario para las ultimas configuraciones
	En la consola con el servidor parado introduce el siguiente comando
> 	python manage.py createsuperuser
	e introduce tu username, email y password

- Pon en marcha el servidor y crea 2 grupos en el admin de Django:


        	python manage.py runserver
        	accede a admin ej. http://127.0.0.1:8000/admin/
        	Da click en add Group, como nombre al primer grupo es 'administrador'
        	guardalo y agrega otro que tenga como nombre 'usuario' y guardalo

 - Para ver la documetacin accede a 
`	http://127.0.0.1:8000/swagger/
	o
	http://127.0.0.1:8000/redoc/`

### Gracias por checar nuestro proyecto :D