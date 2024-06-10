from django.shortcuts import render, redirect
from AppUno.forms import Form


def index(request):
    return render(request, 'index.html')


def agregarSituacion(request):  # Situacion se refiere a si es un Reclamo o Felicitacion
    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    data = {
        'form': form,
    }
    return render(request, 'formulario.html', data)
