# PixelNote

Hecho con python 3.7  
Para instalar los requerimientos:
```
pip install -r requirements.txt
```
### ¿Cómo ejecutar?  
Para iniciar Django use el siguiente comando en la carpeta src:  
```
python manage.py runserver
```
Ingrese a la página *DireccionProporcionadaPorDjango **/admin/*** (e.g. http://127.0.0.1:8000/admin/) e ingrese el usuario y contraseña **(si no se encuentra iniciada la sesión)** ubicados en el archivo private_settings.py  
Una vez haya iniciado sesión puede comenzar a usar la aplicación normalmente.
### URLS
El archivo contiene la siguientes direcciones URL:
- **/**: Página principal del proyecto.  
- **/home/**: Página principal del proyecto.  
- **/admin/**: Administración de Django.  
- **/notes/**:  Lista de notas actuales.  
- **/notes/create/**: Página para la creación de la información de la nota.  
- **/notes/id_req/details/**: Página donde se muestra la información de la nota de **id = id_req**.  
- **/notes/id_req/edit/**: Página con formulario para la modificación de la nota de **id = id_req**.  
- **/notes/id_req/delete/**: Página donde se genera la confirmación para la eliminar la nota de **id = id_req**.

### Estructura
- La carpeta note_item contiene todos los archivos correspondientes a los objetos note_item de la base de datos y el manejo de estos, como a su vez
los el manejo de la aplicación web correspondiente a dichos archivos.  
- La carpeta *src/pages/* contiene todos los archivos correspondientes a las páginas inicio, login y las plantillas base de html
localizadas en la carpeta */templates/*, en dicha carpeta se encuentra un html obsoleta que contiene funciones interesantes, dicho archivo se llama *deprecated.html*  
- La carpeta *src/PixelNote/* contiene los archivos propios de Django correspondientes a la ejecución del mismo.  
- El archivo private_settings.py contiene la clave, este debe ser ubicado en la carpeta */src/*  
- El archivo manage.py archivo propio de Django contiene funciones importantes para el funcionamiento del mismo.  

### ARCHIVOS HTML
Los archivos .html extienden del archivo *src/templates/base.html* por medio de:
```
{% extends 'base.html' %}
```
Contienen bloques que se "reemplazan" en el archivo *src/templates/base.html* permitiendo disminución de código redundante.  
*Véase: /src/note_item/templates/my_notes.html*
### Problemas conocidos
- Las horas tienen una diferencia de + 5 con respecto a la hora actual, en: *src/note_item/models.py*  
- Se debe cambiar valor de editable de los campos de creación y edición de las notas ya que no aparecen desde */admin/*, no obstante, aparecen desde *../edit/*  
- Se debe generar verificación de usuario en todas las páginas y no solamente en */* y */home/*

### ARCHIVOS PYTHON
**Aquellos archivos que no se encuentren comentariados son propios de Django.**  
Se recomienda no modificar los nombres de las funciones, variables y clases ya que pueden corresponder a Django, a su vez,
se recomienda no eliminar archivos a pesar de que se encuentren vacíos.  
Al realizar actualizaciones en la archivos *models.py* ejecutar los siguientes comandos con el fin de realizar las  respectivas modificaciones en la base de datos:
```
python manage.py makemigrations
python manage.py migrate
```