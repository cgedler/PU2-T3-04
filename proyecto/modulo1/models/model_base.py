from django.db import models
from crum import get_current_user
from django.utils import timezone
from django.utils.html import format_html

class Base(models.Model):
    """ Description: Base para las demás tablas """
    # Attributes:
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name = u'Created',
        db_column = 'created')
    created_by = models.ForeignKey(
        'auth.User',
        null = True,
        blank = True,
        default = None,
        on_delete = models.DO_NOTHING,
        related_name = '%(app_label)s_%(class)s_created_by',
        verbose_name = u'Create by',
        db_column = 'create_by')
    modified = models.DateTimeField(
        null = True,
        blank = True,
        verbose_name = u'Modified',
        db_column = 'modified')
    modified_by = models.ForeignKey(
        'auth.User',
        null = True,
        blank = True,
        default = None,
        on_delete = models.DO_NOTHING,
        related_name = '%(app_label)s_%(class)s_modified_by',
        verbose_name = u'Modified by',
        db_column = 'modified_by')
    is_active = models.BooleanField(
        null = True,
        blank = True,
        default = True,
        verbose_name = u'is_active',
        db_column = 'active')

    # Methods:
    def col_created(self):
        return format_html('<span style = "color: #0091EA;">{0}</span>', self.created)
    col_created.short_description = 'Created'

    def col_created_by(self):
        return format_html('<span style = "color: #558B2F;">{0}</span>', self.created_by)
    col_created_by.short_description = 'Created by'

    def col_modified(self):
        return format_html('<span style = "color: #0091EA;">{0}</span>', self.modified)
    col_modified.short_description = 'Modified'

    def col_modified_by(self):
        return format_html('<span style = "color: #F57C00;">{0}</span>', self.modified_by)
    col_modified_by.short_description = 'Modified by'

    class Meta:
        abstract = True


class Empresa(models.Model):
    nombre = models.CharField(
        max_length = 250,
        null = False,
        blank = False,
        default = u'Nombre de la Empresa',
        help_text = u'Nombre de la Empresa',
        verbose_name = u'Nombre',
        db_column = 'nombre')
    direccion = models.TextField(
        max_length = 254,
        null = True,
        blank = True,
        help_text = u'Direccion de la Empresa',
        verbose_name = u'Dirección',
        db_column = 'direccion')
    telefono = models.CharField(
        max_length = 16,
        null = True,
        blank = True,
        default = '000-000-0000',
        verbose_name = u'Teléfono',
        help_text = u'Por favor ingrese el teléfono parecido al ejemplo',
        db_column = 'telefono')
    contacto = models.CharField(
        max_length = 120,
        null = False,
        help_text = u'Por favor ingrese el nombre del contacto',
        verbose_name = u'Nombre Contacto',
        db_column = 'contacto')
    web = models.URLField(
        max_length = 200,
        null = True,
        blank = True,
        verbose_name = u'Web',
        help_text = u'Por favor ingrese la URL',
        db_column = 'web')

    class Meta:
        abstract = True


class Editorial(Empresa, Base):
    
    # Methods:
    def __str__(self):
        cadena = '{0} - {1}'
        return cadena.format(
            self.id,
            self.nombre)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(Editorial, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Editoriales'
        ordering = ['id']
        verbose_name = 'editorial'
        verbose_name_plural = 'editoriales'


class Distribuidora(Empresa, Base):
    
    # Methods:
    def __str__(self):
        cadena = '{0} - {1}'
        return cadena.format(
            self.id,
            self.nombre)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(Distribuidora, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Distribuidoras'
        ordering = ['id']
        verbose_name = 'distribuidora'
        verbose_name_plural = 'distribuidoras'


class Libro(Base):
    isbn = models.CharField(
        max_length = 20,
        null = False,
        blank = False,
        default = u'000000000-0',
        help_text = u'ISBN del Libro',
        verbose_name = u'ISBN',
        db_column = 'isbn')
    titulo = models.CharField(
        max_length = 200,
        null = False,
        blank = False,
        default = u'Titulo',
        help_text = u'Titulo del Libro',
        verbose_name = u'Titulo',
        db_column = 'titulo')
    autor = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        default = u'Nombre Apellido',
        help_text = u'Autor del Libro',
        verbose_name = u'Autor',
        db_column = 'autor')
    publicacion = models.DateField(
        db_column = 'publicacion'
    )
    paginas = models.PositiveSmallIntegerField(
        db_column = 'paginas'
    )
    precio = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        db_column = 'precio')

    id_editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE,
        related_name = '%(app_label)s_%(class)s_editorial',
        verbose_name = u'Editorial',
        db_column = 'editorial'
        )

    id_distribuidora = models.ForeignKey(
        Distribuidora, 
        on_delete=models.CASCADE,
        related_name = '%(app_label)s_%(class)s_distribuidora',
        verbose_name = u'Distribuidora',
        db_column = 'distribuidora'
        )

    def __str__(self):
        cadena = '{0} - {1}'
        return cadena.format(
            self.id,
            self.titulo)
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(Libro, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Libros'
        ordering = ['id']
        verbose_name = 'libro'
        verbose_name_plural = 'libros'