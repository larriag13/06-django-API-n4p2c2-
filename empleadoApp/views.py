from django.shortcuts import render,redirect
from .models import Empleado
from . import forms
# Create your views here.
def index(request):
    form=forms.EmpleadoForm()
    if request.method=='POST':
        form=forms.EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return listar_empleados(request)
    data={'form':form}
    return render(request,'empleadoApp/index.html',data)

def listar_empleados(request):
    empleados=Empleado.objects.all()
    data={'empleados':empleados}
    return render(request,'empleadoApp/listar_empleados.html',data)

def editar_empleado(request,id):
    empleado=Empleado.objects.get(id=id)
    form=forms.EmpleadoForm(instance=empleado)
    if request.method=='POST':
        form=forms.EmpleadoForm(request.POST,instance=empleado)
        if form.is_valid():
            form.save()
            return listar_empleados(request)
    data={'form':form}
    return render(request,'empleadoApp/index.html',data)

def eliminar_empleado(request,id):
    empleado=Empleado.objects.get(id=id)
    empleado.delete()
    return listar_empleados(request)