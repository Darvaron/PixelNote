from django import forms
from .models import Note_item

class NoteItemForm(forms.ModelForm):
    class Meta:
        model = Note_item
        fields = [
            'title',
            'description',
            'summary'
        ]
