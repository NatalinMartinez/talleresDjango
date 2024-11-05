from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def informe(request):
    informes = [
        {'nombre': 'Juan', 'apellido': 'Pérez', 'email': 'juan@example.com', 'telefono': '123456789'},
        # Agrega más datos según sea necesario
    ]
    return render(request, 'informe.html', {'informes': informes})

def contacto(request):
    if request.method == 'POST':
        # Manejo del formulario aquí (guardar datos, enviar email, etc.)
        pass
    return render(request, 'contacto.html')
