"""academia21 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls.conf import include
#from app.controller.AsistenciaController import AddAsistencia, Asistencialist
from django.contrib import admin
from django.urls import path
from app.controller.indexController import indexController, welcomeController
from django.conf import settings
from django.conf.urls.static import static
from app.controller.CursosController import CursosController, ProgramaController

from app.controller.nosotrosController import nosotrosController
from app.controller.direccionController import direccionController
from django.contrib.auth.views import LogoutView
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', indexController.index, name='index'),
    path('nosotros/', nosotrosController.index, name='nosotros'),
    path('direccion/', direccionController.index, name='direccion'),
   
    path('cursos/details/<int:cursoid>',CursosController.details, name='details'),
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', LogoutView.as_view(), name='logout'),
   
    path('cursos/', CursosController.index, name='cursos'),
   # path('cursos/', ProgramaController.index, name='cursos'),
    path('details/<int:cursoid>', CursosController.details, name='details'),
    path('', include('User.urls')),
    path('', include('app.urls')),
    path('', include('Login.urls')),
    path('Bienvenido', welcomeController.index, name='welcome'),
    # path('report/<int:')
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
