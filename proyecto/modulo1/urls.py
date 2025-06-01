from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from modulo1.views.view_base import *
from modulo1.views.view_libros import *
from modulo1.views.view_editorial import *
from modulo1.views.view_distribuidora import *

app_name = 'modulo1'

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    # Libros
    path('Libros/', login_required(ListadoLibro.as_view()), name='LibroListado'),
    path('Libros/crear', login_required(CrearLibro.as_view()), name='LibroCrear'),
    path('Libros/detalle/<str:pk>', login_required(DetalleLibro.as_view()), name='LibroDetalle'),
    path('Libros/actualizar/<str:pk>', login_required(ActualizarLibro.as_view()), name='LibroActualizar'),
    path('Libros/eliminar/<str:pk>', login_required(EliminarLibro.as_view()), name='LibroEliminar'),
    path('Libros/search', login_required(SearchResultsLibros.as_view()), name='LibroSearch'),
    path('Libros/pdf/', login_required(GeneratePdfListLibros.as_view()), name='PdfListLibros'),
    path('Libros/pdf/<str:pk>', login_required(GeneratePdfLibro.as_view()), name='PdfLibro'),
    path('Libros/word/<str:pk>', login_required(GenerateWordLibro.as_view()), name='WordLibro'),
    path('Libros/excel/<str:pk>', login_required(GenerateExcelLibro.as_view()), name='ExcelLibro'),
    path('Libros/grafico', login_required(GraficoLibro), name='GraficoLibro'),
    # Editorial
    path('Editorial/', login_required(ListadoEditorial.as_view()), name='EditorialListado'),
    path('Editorial/crear', login_required(CrearEditorial.as_view()), name='EditorialCrear'),
    path('Editorial/detalle/<str:pk>', login_required(DetalleEditorial.as_view()), name='EditorialDetalle'),
    path('Editorial/actualizar/<str:pk>', login_required(ActualizarEditorial.as_view()), name='EditorialActualizar'),
    path('Editorial/eliminar/<str:pk>', login_required(EliminarEditorial.as_view()), name='EditorialEliminar'),
    path('Editorial/pdf/', login_required(GeneratePdfListEditorial.as_view()), name='PdfListEditorial'),
    path('Editorial/pdf/<str:pk>', login_required(GeneratePdfEditorial.as_view()), name='PdfEditorial'),
    path('Editorial/word/<str:pk>', login_required(GenerateWordEditorial.as_view()), name='WordEditorial'),
    path('Editorial/excel/<str:pk>', login_required(GenerateExcelEditorial.as_view()), name='ExcelEditorial'),
    # Distribuidora
    path('Distribuidora/', login_required(ListadoDistribuidora.as_view()), name='DistribuidoraListado'),
    path('Distribuidora/crear', login_required(CrearDistribuidora.as_view()), name='DistribuidoraCrear'),
    path('Distribuidora/detalle/<str:pk>', login_required(DetalleDistribuidora.as_view()), name='DistribuidoraDetalle'),
    path('Distribuidora/actualizar/<str:pk>', login_required(ActualizarDistribuidora.as_view()), name='DistribuidoraActualizar'),
    path('Distribuidora/eliminar/<str:pk>', login_required(EliminarDistribuidora.as_view()), name='DistribuidoraEliminar'),
    path('Distribuidora/pdf/', login_required(GeneratePdfListDistribuidora.as_view()), name='PdfListDistribuidora'),
    path('Distribuidora/pdf/<str:pk>', login_required(GeneratePdfDistribuidora.as_view()), name='PdfDistribuidora'),
    path('Distribuidora/word/<str:pk>', login_required(GenerateWordDistribuidora.as_view()), name='WordDistribuidora'),
    path('Distribuidora/excel/<str:pk>', login_required(GenerateExcelDistribuidora.as_view()), name='ExcelDistribuidora')
]