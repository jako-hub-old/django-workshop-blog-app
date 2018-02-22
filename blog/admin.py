from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):    
    """Modelo de los posts...
    Ejemplo de documentación de clases
    Note: 
        más información: https://www.python.org/dev/peps/pep-0257/
    Attributes:
        Attr1 ([type]): Description...
        Attr2 (:obj:int, optional): Description...
    """
    list_display = ('title', 'slug', 'author', 'publish', 'status',) # Permite asignar las columnas que se mostrarán en la vista de lista.
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = { 'slug' : ('title',) }
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)