from django.shortcuts import redirect, render
from .models import Inscritos, Institucion
from .serializers import InstitucionesSerial, InscritosSerial


from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


def index(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST'])
def ListaUsr(request):
    if request.method == 'GET':
        proye = Inscritos.objects.all()
        return render(request, 'listado.html', {'proyec': proye})

@api_view(['GET', 'POST'])
def Agregar(request):
    if request.method == 'GET':
        inscritos = Inscritos.objects.all()
        instituciones = Institucion.objects.all()
        return render(request, 'agregar.html', {'inscritos': inscritos, 'instituciones': instituciones})

    if request.method == 'POST':
        serializer = InscritosSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('agregar')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def Agregarinstitucion(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        return render(request, 'instituciones.html', {'agregarinstitucion': instituciones})

    if request.method == 'POST':
        serializer = InstitucionesSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('agregarinstitucion')
        return render(request, 'instituciones.html', {'form': serializer})
    
def Usuario(request):
    data = { 
        'Nombre': 'Esteban Reyes',
        'RUT':'21.401.538-2',
        'Seccion': 'IEI-171-N4',
    }
    return JsonResponse(data)

class InstitucionSerial(APIView):
    def get(self, request):
        institucion =Institucion.objects.all()
        serial = InstitucionesSerial(institucion, many=True)
        return Response(serial.data)
    
    def post(self,request):
        serial = InstitucionesSerial(data= request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status = status.HTTP_201_CREATED)
        return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)
    
class InscritoSerial(APIView):
    def get(self, request):
        inscritos = Inscritos.objects.all()
        serial = InscritosSerial(inscritos, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
