from django.shortcuts import render


def index(request):

    dados = {
    1:{'nome': 'Nebulosa de Carina',
       'legenda': 'Webbtelescope | NASA | James webb'},
    2:{'nome': 'Galáxia NGC 1079',
       'legenda': 'nasa.org | NASA | Hublle'},
    }

    return render (request, 'galeria/index.html', {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')