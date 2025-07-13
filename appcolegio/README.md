# PROYECTO DE GESTIÓN ESCOLAR

## Para las versiones de dependecias 
### Ver `requirements.txt` para dependencias

## Instalación

1. Clonar el repositorio:

    ```bash
    git clone  https://github.com/groxemberg-proyec/trabajo_practico-modulo5.git

2. Crear y activar entorno virtual:
    
    ```bash
    python -m venv venv
    source venv/bin/activate # Linux / Mac
    .\venv\Scripts\activate # Windows

3. Instalar dependencias:

    ```bash
    pip install -r requirements.txt

4. Ejecutar migraciones:

    ```bash
    python manage.py migrate

5. Crear superusuario:
    
    ```bash
    python manage.py createsuperuser

6. Correr servidor:

    ```bash
    python manage.py runserver

Uso

Acceder al panel de administración de Django en: http://127.0.0.1:8000/admin

Gestionar colegios, personas, profesores, estudiantes y cursos desde el panel.

