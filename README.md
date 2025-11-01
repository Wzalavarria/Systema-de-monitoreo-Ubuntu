Monitor del Sistema con Django y Psutil
Descripción
Este proyecto es un examen de monitoreo del sistema desarrollado en Django. 
Permite visualizar en tiempo real el estado del sistema, incluyendo el uso de CPU, memoria RAM, almacenamiento en disco y otros datos relevantes, utilizando la librería externa psutil.

La aplicación muestra la información de forma clara en la interfaz web y permite actualizar los datos manualmente con un botón "Actualizar".
Requisitos
- Python 3.10 o superior
- Django 5.2.7 o superior
- psutil 7.1.2 o superior
Instalación
1. Clonar el repositorio:
git clone https://github.com/TU_USUARIO/monitor-system.git

2. Entrar a la carpeta del proyecto:
cd monitor-system/monitor

3. Crear un entorno virtual y activarlo:
python -m venv venv
source venv/bin/activate  # Linux
# En Windows: venv\Scripts\activate

4. Instalar dependencias:
pip install -r requirements.txt
Ejecución
Para levantar el servidor de desarrollo:
python manage.py runserver

Luego abrir en el navegador:
http://127.0.0.1:8000/
Estructura del Proyecto
- monitor/ → Carpeta del proyecto Django con settings.py, urls.py, etc.
- sistema/ → Aplicación interna que contiene:
    - views.py → Lógica para recolectar datos del sistema usando psutil
    - urls.py → Rutas internas de la app
    - templates/sistema/ → Plantilla HTML para mostrar los datos
- manage.py → Script principal para ejecutar Django
- requirements.txt → Dependencias del proyecto
Funcionalidades
- Visualiza el uso de CPU (% y número de núcleos)
- Muestra la memoria RAM (total, usada y porcentaje)
- Muestra el espacio en disco (total, usado y libre)
- Información del sistema operativo
- Actualización manual de los datos con botón
- Manejo de errores si psutil no puede obtener algún dato
  
Autor
Yarely Hissell Hernández Vigil 202220110026
Kateryn Lisbeth Soriano Midence 202230110015
Wilmer Mc.veigh Zalavarria Carbajal 202210110009

Universidad Tecnológica de Honduras (UTH)

