from django.db import models
from django.utils import timezone

class Note_item(models.Model):
    ''''
    item shown in the user notes page, contains basic info of one user's note
    '''
    title = models.CharField(blank= False, max_length=30)
    description = models.CharField(blank= True, null= True, max_length=150)
    summary = models.TextField(blank= True, null=True)
    created = models.DateTimeField(editable= False)
    modified = models.DateTimeField(editable= False)

    def save(self, *args, **kwargs):
        '''
        On save updates timestamps
        '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Note_item, self).save(*args, **kwargs)
