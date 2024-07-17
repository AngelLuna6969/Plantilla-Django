# Plantilla Django

Este proyecto consiste en generar una plantilla con funcionalidad de base de datos, front-end y back-end mediante interfaces amigables y recueroso como dataTables

## Instalacion 🚀

Para descargar el proyecto se tiene la opcion de decargar mediante un archivo .zip o clonar el proyecto

```
git clone url
```

### Recomendacion 📋

Crea un entorno virtual
```
cd mi-proyecto-django
python -m venv venv
source venv/bin/activate  # (o venv\Scripts\activate en Windows)
```

Instalar dependencias
```
pip install -r requirements.txt
```

### Ejecucion 🔧

Configura la base de datos en settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Realiza las migraciones
```
python manage.py migrate
```

Una vez instalado los requerimeintos y editado la configuracion se podra ejecutar

```
python manage.py runserver
```
Abre tu navegador y ve a http://localhost:8000/

