from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .form import CrearForm
from .models import vehiculos
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        # print("no logueado")
        return render(request, 'index.html', {'error': "Inicie sesión para visualizar la Informacion"})


def listar(request):
    if request.user.is_authenticated:
        # print("logueado")

        lista_v = vehiculos.objects.filter()
        return render(request, 'listar.html', {'lista_v': lista_v})
    else:
        # print("no logueado")
        return render(request, 'listar.html', {'error': "Inicie sesión para visualizar la Informacion"})


def annadir(request):
    if request.method == 'GET':
        return render(request, 'ingreso.html', {'form':  CrearForm})
    else:
        try:
            form = CrearForm(request.POST)
            nueva_vehiculo = form.save(commit=False)
            # nueva_vehiculo.usuario = request.user
            nueva_vehiculo.save()
            return render(request, 'ingreso.html', {'form': CrearForm, 'error': 'Vehiculo Ingresado correctamente'})
        except ValueError:
            return render(request, 'ingreso.html', {'form': CrearForm, 'error': 'Datos erroneos'})
        

def salir(request):
    logout(request)
    return redirect('index')

def loguearse(request):
    if request.method == 'GET':
        return render(request, 'loguearse.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        # print(request.POST)
        if user is None:
            return render(request, 'loguearse.html', {'form': AuthenticationForm, 'error': 'usuario o contraseña incorrecto'
                                                  })
        else:
            login(request, user)
            return redirect('index')
        
def eliminar(request, vehiculo_id): 
    if request.method == 'GET':
        # print(request.method)
        #vehiculo_buscar = auto.objects.get(pk=auto_id)
        vehiculo_buscar = get_object_or_404(vehiculos,pk=vehiculo_id)
        formulario = CrearForm(instance=vehiculo_buscar)
        return render(request, 'eliminar.html', {'lista': vehiculo_buscar, 'formulario':formulario})      
    else:           
        try:
            vehiculo_buscar = get_object_or_404(vehiculos,pk=vehiculo_id)
            vehiculo_buscar.delete()
            lista_v = vehiculos.objects.filter()
            return render(request, 'listar.html', {'lista_v': lista_v, 'error': "Vehiculo Eliminado"})
        except ValueError:
            return render(request, 'listar.html', {'lista_v': lista_v, 'error': "Error Eliminacin"})


def editar(request, vehiculo_id): 
    if request.method == 'GET':
        print(request.method)
        #tarea_buscar = tarea.objects.get(pk=tarea_id)
        vehiculo_buscar = get_object_or_404(vehiculos,pk=vehiculo_id)
        formulario = CrearForm(instance=vehiculo_buscar)
        return render(request, 'detalle.html', {'lista':vehiculo_buscar, 'formulario':formulario})      
    else:           
        try:
            vehiculo_buscar = get_object_or_404(vehiculos,pk=vehiculo_id)
            editar_vehiculo = CrearForm(request.POST, instance=vehiculo_buscar)
            editar_vehiculo.save()
            lista_v = vehiculos.objects.filter()
            return render(request, 'listar.html', {'lista_v': lista_v, 'error': "Vehiculo actualizado"})
        except ValueError:
            lista_v = vehiculos.objects.filter()
            return render(request, 'listar.html', {'lista_v': lista_v, 'error': "Error al actualizar"})



# def registrarse(request):
#     if request.method == 'GET':
#         return render(request, 'registrarse.html', {
#             'form': UserCreationForm
#         })
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(
#                     username=request.POST['username'], password=request.POST['password1'], permission='visualizar_catalogo')
#                 user.save()
#                 login(request, user)
#                 return redirect('index')
#                 # return HttpResponse('usuario Creado correctamente')
#             except:
#                 return render(request, 'registrarse.html', {'form': UserCreationForm, 'error': "usuario no pudo ser creado"})
#         else:
#             return render(request, 'registrarse.html', {'form': UserCreationForm, 'error': "contraseñas diferentes"})


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                content_type = ContentType.objects.get(app_label='vehiculos', model='vehiculos')
                permission = Permission.objects.get(content_type=content_type, codename='visualizar_catalogo')

                user.user_permissions.add(permission)

                user.save()
                login(request, user)
                return redirect('index')
                # return HttpResponse('usuario Creado correctamente')
            except:
                return render(request, 'registrarse.html', {'form': UserCreationForm, 'error': "usuario no pudo ser creado"})
        else:
            return render(request, 'registrarse.html', {'form': UserCreationForm, 'error': "contraseñas diferentes"})
