from ast import Return, parse
from cgitb import text
import math
from re import I
from django.http import HttpResponse


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
    