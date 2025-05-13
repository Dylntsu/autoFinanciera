# Evidencia Final de la Materia administración de proyectos en TI

# Administración de Automóviles

## Descripción
Este proyecto es una aplicación web desarrollada con Django para la administración de automóviles. Permite crear, listar, editar, ver detalles y eliminar automóviles, utilizando una interfaz moderna con Bootstrap.

## Requisitos Previos
- Python 3.x
- pip
- Git

## Instalación

1. **Clonar el repositorio**
   ```powershell
   git clone https://github.com/Dylntsu/autoFinanciera.git
   cd autoFinanciera/administracion
   ```

2. **Crear y activar un entorno virtual**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```powershell
   pip install django
   ```

4. **Aplicar migraciones**
   ```powershell
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional)**
   ```powershell
   python manage.py createsuperuser
   ```

6. **Correr el servidor**
   ```powershell
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Abre tu navegador en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Estructura del Proyecto

- `admin_automovil/` y `admin_automoviles/`: Apps Django para la gestión de automóviles.
- `templates/`: Archivos HTML para las vistas.
- `assets/` y `staticfiles/`: Archivos estáticos (CSS, JS, imágenes).
- `manage.py`: Script principal de Django.

## Funcionalidades

- Listar automóviles
- Agregar nuevo automóvil
- Editar automóvil existente
- Ver detalles de un automóvil
- Eliminar automóvil

## Personalización

- Los estilos se encuentran en `assets/css/style.css`.
- Las plantillas HTML están en la carpeta `templates/`.

## Notas y Consejos

- Para agregar nuevas funcionalidades, crea nuevas vistas y plantillas según la arquitectura Django.
- Si tienes problemas con Git, asegúrate de resolver conflictos antes de hacer push.
- Puedes cambiar el editor de Git con: `git config --global core.editor "notepad"`
- Si necesitas instalar más dependencias, agrégalas en el entorno virtual y documenta los cambios en este archivo.

## Buenas Prácticas

- Realiza commits frecuentes y descriptivos.
- Usa ramas para nuevas funcionalidades o correcciones.
- Mantén el código limpio y documentado.
- Haz pruebas antes de subir cambios al repositorio remoto.

## Créditos
- Proyecto realizado por: [Tu Nombre]
- Materia: Administración de Proyectos en TI
- Fecha: Mayo 2025

---

¡Gracias por revisar este proyecto!
