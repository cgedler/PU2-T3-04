from django.contrib import admin

from .models import *
# Register your models here.


class EditorialAdmin(admin.ModelAdmin):
   list_display = (
      'id',
      'nombre',
      'direccion',
      'telefono',
      'contacto',
      'web',
      'col_created',
      'col_created_by',
      'col_modified',
      'col_modified_by',
      'is_active'
   )
   search_fields = ['id']
   empty_value_display = '-empty-'
admin.site.register(Editorial, EditorialAdmin)

class DistribuidoraAdmin(admin.ModelAdmin):
   list_display = (
      'id',
      'nombre',
      'direccion',
      'telefono',
      'contacto',
      'web',
      'col_created',
      'col_created_by',
      'col_modified',
      'col_modified_by',
      'is_active'
   )
   search_fields = ['id']
   empty_value_display = '-empty-'
admin.site.register(Distribuidora, DistribuidoraAdmin)

class LibroAdmin(admin.ModelAdmin):
   list_display = (
      'id',
      'isbn',
      'titulo',
      'autor',
      'publicacion',
      'paginas',
      'precio',
      'id_editorial',
      'id_distribuidora',
      'col_created',
      'col_created_by',
      'col_modified',
      'col_modified_by',
      'is_active'
   )
   search_fields = ['id']
   empty_value_display = '-empty-'
admin.site.register(Libro, LibroAdmin)