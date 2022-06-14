from ast import Return, parse
from cgitb import text
import math
from re import I
from tempfile import template
from django.http import HttpResponse
from django.shortcuts import render
from polls import urls
from polls.models import Articulo

def index(request):
    return HttpResponse("welcome compa")

def mensaje(request):
    texto = "esto es un ejemplo de texto"
    formato = """
    <h1> %s </h1>
    """ % texto
    return HttpResponse(formato)

def potencia(request,valor):
    resultado = math.pow(valor,3)
    texto = """
    %s al cubo es: %s
    """ % (valor,resultado)
    return HttpResponse(texto)
#agregar una funcion que reciba un valor e indique si es: positivo, negativo o neutro
def func_num(request,valors):
    valors = int(valors)
    if(valors==0):
            resultado1 = "NEUTRO"
            texto = """
            %s  es: %s
            """ % (valors,resultado1)
    elif(valors>0):
            resultado2 = "positivo"
            texto = """
            %s  es: %s
            """ % (valors,resultado2)
    elif(valors<0):
            resultado3 = "negativo"
            texto = """
            %s  es: %s
            """ % (valors,resultado3)
    return HttpResponse(texto)

def home(request):
    return render(request, 'polls/index.html')


def ingresar_producto(request):
    #nombre_aux = 
    #categoria_aux =
    #precio_aux = 
    return render(request, 'polls/ingresar_producto.html')