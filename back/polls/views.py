from django.http import *
from polls.models import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):

    return HttpResponse("Index")

@csrf_exempt
def crear(request):

    data = json.loads(request.body.decode('utf-8'))


    grafica = graficas(tipo=data['tipo'], titulo=data['titulo'], cantidad=data['cantidad'])

    nombres = []

    numeros = [] 

    for index, x in enumerate(data['datos']):

        if index % 2 == 0:
            print('nombre')
            nombres.append(x)
        else:
            print('numero')
            numeros.append(x)

    for index, x in enumerate(nombres):

        if (index+1) == 1:
            grafica.nombre1 = x

        if (index+1) == 2:
            grafica.nombre2 = x

        if (index+1) == 3:
            grafica.nombre3 = x

        if (index+1) == 4:
            grafica.nombre4 = x

        if (index+1) == 5:
            grafica.nombre5 = x

        if (index+1) == 6:
            grafica.nombre6 = x
            
        if (index+1) == 7:
            grafica.nombre7 = x

        if (index+1) == 8:
            grafica.nombre8 = x

        if (index+1) == 9:
            grafica.nombre9 = x

        if (index+1) == 10:
            grafica.nombre10 = x



    for index, x in enumerate(numeros):

        if (index+1) == 1:
            grafica.numero1 = x

        if (index+1) == 2:
            grafica.numero2 = x

        if (index+1) == 3:
            grafica.numero3 = x

        if (index+1) == 4:
            grafica.numero4 = x

        if (index+1) == 5:
            grafica.numero5 = x

        if (index+1) == 6:
            grafica.numero6 = x
            
        if (index+1) == 7:
            grafica.numero7 = x

        if (index+1) == 8:
            grafica.numero8 = x

        if (index+1) == 9:
            grafica.numero9 = x

        if (index+1) == 10:
            grafica.numero10 = x


    grafica.save()


    return HttpResponse(grafica.id)



@csrf_exempt
def getGrafica(request):

    data = json.loads(request.body.decode('utf-8'))

    grafica = serializers.serialize("json", graficas.objects.filter(id=data['id']))

    jsonn = {"Grafica": json.loads(grafica)}

    return JsonResponse(jsonn)



@csrf_exempt
def verGraficas(request):

    lista = serializers.serialize("json", graficas.objects.all())

    jsonn = {"Graficas": json.loads(lista)}

    return JsonResponse(jsonn)



@csrf_exempt
def eliminar(request):

    data = json.loads(request.body.decode('utf-8'))

    grafica = graficas.objects.get(id=data['id'])

    grafica.delete()

    return HttpResponse("eliminar")