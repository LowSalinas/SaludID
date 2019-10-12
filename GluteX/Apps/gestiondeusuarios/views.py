from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'inicio.html')

def funcion (request):   
    numero = request.GET['numero'] 
    Usuarios = Usuario.objects.all()
    Doctors = Doctor.objects.all()
    Nutriologos = Nutriologo.objects.all()
    NumIDs = NumID.objects.all()
    return render(request, 'busqueda.html', { 'numero': numero,'Usuarios': Usuarios,'Doctors': Doctors,'Nutriologos': Nutriologos,'NumIDs:':NumIDs})