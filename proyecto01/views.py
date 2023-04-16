from django.http import HttpResponse
from django.template import Context, Template


def saludar(request):
    return HttpResponse('Hola mundo!')

def inicio(request):
    archivo=open(r"/Users/daianaskibicki/Desktop/proyecto/templates/plantilla.html")
    texto=archivo.read()
    archivo.close()

    template=Template(texto)
    contexto=Context()
    documento=template.render(contexto)
    return HttpResponse(documento)


    #contexto= {}
    #plantilla = loader.get_template("plantilla.html")
    #documento=plantilla.render(contexto)
    #return HttpResponse(documento)


