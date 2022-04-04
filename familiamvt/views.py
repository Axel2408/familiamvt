from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.template import Template, context, loader

def primervsita(request):
    return HttpResponse ("Familia!")

def segundavista(request):
    return HttpResponse("listado de mi familia")

def pagina_inicio(request):
    archivo=open(r"C:\Users\PC\Desktop\PYTHON\famiia env\familiamvt\familiamvt\template\familia.html", "r")
    
    nombreyparentezco={"papa":"Alexis", "mama":"Andrea", "hermano":"Audric", "tio":"Claudio"}

    cumpleanos={"papa":"06/04/1972","mama": "05/06/1972", "hermano":"28/03/2007", "tio":"12/02/1971"}

    edad={"papa":49, "mama":49, "hermano":15, "tio":51}

    dic_context={"nombreypa": nombreyparentezco, "cumple":cumpleanos, "edad":edad}

    plantilla=Template(archivo.read())

    archivo.close()

    contexto=context(dic_context)

    documento=plantilla.render(contexto)

    return HttpResponse(documento)