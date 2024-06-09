from django.shortcuts import render, redirect
from AppUno.forms import Form


def index(request):
    data = {
        'https://es.wikipedia.org/wiki/Elden_Ring': '/static/img/Elden_Ring.jpeg',
        'https://es.wikipedia.org/wiki/Frostpunk': '/static/img/Frostpunk.jpeg',
        'https://es.wikipedia.org/wiki/Minecraft': '/static/img/Minecraft.jpg',
    }
    cafe = {
        'Expreso o espresso / Café solo': 'El café expreso consiste en uno de los tipos de café más básicos y sencillos. Su elaboración es muy fácil y, únicamente, consiste en realizar la infusión de café llevando a ebullición el agua para que entren en contacto con los granos de café molidos.',
        'Cortado o macchiato': 'Comúnmente conocido como café cortado o macchiato, este tipo de café es uno de los más demandados.',
        'Lungo / largo': 'El café lungo o largo se trata de un tipo de café en el que la extracción de agua en contacto con los granos de café molidos se realiza de manera más prolongada, lo que conlleva más cantidad de infusión.',
        'Café con leche': 'Con su elaboración, conseguimos un sabor más dulce y menos intenso, aunque el nivel de cafeína sigue siendo muy potente.',
    }
    return render(request, 'index.html', {'data': data.items(), 'cafe': cafe.items()})


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
