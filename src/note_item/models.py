from django.db import models
from django.utils import timezone
from django.urls import reverse

'''
Descripción: Contiene el modelo de Note_item que fue generado en la base de datos y el que se usa para manejar dichas
operaciones de la base de datos y archivos asociados a este modelo.
'''


class Note_item(models.Model):
    ''''
    Clase que contiene una plantilla del objeto Note_item con sus respectivos atributos.
    '''
    # Atributos
    title = models.CharField(blank=False, max_length=30)
    description = models.CharField(blank=True, null=True, max_length=150)
    summary = models.TextField(blank=True, null=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    def get_absolute_url(self):
        '''
        Genera la dirección de url usada en los archivos .html para redireccionar por medio del comando
        href="{{item.get_absolute_url}}"
        :return: URL
        '''
        '''
        Hace referencia al nombre notes asociado en el archivo src/note_item/urls -> app_name:
        src/note_item/urls -> urlpatterns, pasando el argumento requerido por dicho urlpattern correspondiente
        '''
        return reverse("notes:details", kwargs={"id_req": self.id})

    def save(self, *args, **kwargs):
        '''
        Sobreescritura del método save para actualizar la hora de modificación y no modificar la creación
        '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Note_item, self).save(*args, **kwargs)
