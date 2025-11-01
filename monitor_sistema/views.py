# Create your views here.
from django.shortcuts import render
import psutil
import platform

def sistema_view(request):
    # CPU
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()

    # Memoria RAM
    memoria = psutil.virtual_memory()
    memoria_total_gb = round(memoria.total / (1024 ** 3), 2)
    memoria_usada_gb = round(memoria.used / (1024 ** 3), 2)
    memoria_percent = memoria.percent

    # Disco
    disco = psutil.disk_usage('/')
    disco_total_gb = round(disco.total / (1024 ** 3), 2)
    disco_usado_gb = round(disco.used / (1024 ** 3), 2)
    disco_libre_gb = round(disco.free / (1024 ** 3), 2)
    disco_percent = disco.percent

    # Sistema
    so = platform.system()
    so_version = platform.version()

    context = {
        'cpu_percent': cpu_percent,
        'cpu_count': cpu_count,
        'memoria_total_gb': memoria_total_gb,
        'memoria_usada_gb': memoria_usada_gb,
        'memoria_percent': memoria_percent,
        'disco_total_gb': disco_total_gb,
        'disco_usado_gb': disco_usado_gb,
        'disco_libre_gb': disco_libre_gb,
        'disco_percent': disco_percent,
        'so': so,
        'so_version': so_version,
    }

    return render(request, 'monitor_sistema/sistema.html', context)
