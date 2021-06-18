from django import forms
from .models import Note_item

'''
Descripción: Corresponde al manejo de los formularios que son enviados al archivo note_item_create y
note_item_edit.
'''


class NoteItemForm(forms.ModelForm):
    '''
    Formulario que contiene los campos del fomulario, extiende de forms.ModelForm
    '''
    # Campos del formulario
    title = forms.CharField(label='Título', widget=forms.TextInput(attrs={'placeholder': 'Título de la nota'}))
    description = forms.CharField(label='Descripción',
                                  widget=forms.TextInput(attrs={'placeholder': 'Descripción de la nota'}),
                                  required=False)
    summary = forms.CharField(
        label='Resumen', required=False, widget=forms.Textarea(
            attrs={
                'class': 'new-class-name two',
                # Acá se "importaría" el css correspondiente a dicho campo del formulario
                'placeholder': 'Resumen de la nota',
                'rows': 20,
                'cols': 120
            }
        ))

    # Class Meta es requerido por la clase forms.ModelForm
    class Meta:
        # Objeto del que se realizará el formulario
        model = Note_item

        # Nombre de las variables correspondientes al objeto Note_item - campos del formulario.
        fields = [
            'title',
            'description',
            'summary'
        ]

    def clean_title(self, *args, **kwargs):  # clean_<field>
        '''
        Valida que el título contenga la palabra Note
        :param args: *args
        :param kwargs: **kwargs
        :return: title -- título validado, lanza una excepción si no cumple con el requermiento, esto impide el envio
        del formulario y presenta un mensaje en el formulario
        '''

        title = self.cleaned_data.get('title')

        if not 'Note' in title:
            raise forms.ValidationError('No es título valido, requiere que contenga la cadena: "Note".')
        return title


# OBSOLETO - Contiene manejo del formulario por medio de datos en crudo.
'''
class RawNoteItemForm(forms.Form):
    title = forms.CharField(label= 'Título', widget= forms.TextInput(attrs={'placeholder': 'Título de la nota'}))
    description = forms.CharField(label='Descripción', widget= forms.TextInput(attrs={'placeholder': 'Descripción de la nota'}),required=False)
    summary = forms.CharField(
        label= 'Resumen', required=False, widget=forms.Textarea(
            attrs={
                'class': 'new-class-name two',
                'placeholder': 'Resumen de la nota',
                'rows': 20,
                'cols': 120
            }
        ))
'''
