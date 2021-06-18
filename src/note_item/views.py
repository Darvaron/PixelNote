from django.shortcuts import get_object_or_404
from .models import Note_item
from .forms import NoteItemForm
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)

'''
Descripción: Manejo de la base de datos para note_item, contiene los métodos necesarios para interactuar con dicha base
'''


class note_item_edit_view(UpdateView):
    '''
    Clase correspondiente de generar el formulario de edición y realizar dicha edición en la base de datos
    '''
    template_name = 'note_item/note_item_edit.html'  # Dirección de URL a ingresar
    form_class = NoteItemForm
    queryset = Note_item.objects.all()  # Obtiene los objetos guardados
    sucess_url = '/'  # Reemplazo de la URL a redirigir al terminar el formulario,

    # sobreescritura de URL get_absolute_url de models.py
    # Pero al parecer no funciona y sigue mandando a los detalles

    def get_object(self):
        id_note = self.kwargs.get("id_req")
        return get_object_or_404(Note_item,
                                 id=id_note)  # Busca el objeto requerido entre la lista, si no lo encuentra redirige a 404

    def form_valid(self, form):
        print('Editado: {}'.format(form.cleaned_data))
        return super().form_valid(form)


class note_item_create_view(CreateView):
    '''
    Clase correspondiente de generar el formulario de creación y realizar dicha creación en la base de datos
    '''
    template_name = 'note_item/note_item_create.html'
    form_class = NoteItemForm
    queryset = Note_item.objects.all()  # notes/<urls>
    sucess_url = '/'  # overwrite the get_absolute_url

    def form_valid(self, form):
        print('Creando: {}'.format(form.cleaned_data))
        return super().form_valid(form)


class note_item_list_view(ListView):
    '''
    Genera la lista de las notas que se encuentren almacenadas en la base de datos
    '''
    template_name = 'note_item/my_notes.html'
    queryset = Note_item.objects.all()  # notes/<urls>


class note_item_detail_view(DetailView):
    '''
    Genera los detalles correspondientes al objeto actual, si no existe genera 404
    '''
    template_name = 'note_item/note_item_detail.html'

    def get_object(self):
        id_note = self.kwargs.get("id_req")
        return get_object_or_404(Note_item, id=id_note)


class note_item_delete_view(DeleteView):
    '''
    Elimina el objeto actual de la base de datos
    '''
    template_name = 'note_item/note_item_delete.html'

    def get_object(self):
        id_note = self.kwargs.get("id_req")
        return get_object_or_404(Note_item, id=id_note)

    def get_success_url(self):  # Otra forma de reemplazar la URL a la que redirecciona get_absolute_url,
        # reemplaza de dicha función que se encuentra en models.py
        return reverse('notes:notes')


# OBSOLETO - Contiene manejo del formulario para la creación de un note_item por medio de datos en crudo.
'''
def note_item_createv(request):
    form = RawNoteItemForm()
    if request.method == "POST":
        form = RawNoteItemForm(request.POST)
        if form.is_valid():
            #The data is good
            print(form.cleaned_data)
            Note_item.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, 'note_item/note_item_create.html', context)
'''

# OBSOLETO - Otra forma de creación de note_item por medio de datos en crudo.
'''
def note_item_createv(request):

    if request.method == 'POST':
        my_new_title = request.POST.get('title')
        # Note_item.objects.create(title= my_new_title)
        print(my_new_title)

    context = {
    }
    return render(request, 'note_item/note_item_create.html', context)
'''

# OBSOLETO - Otra forma de creación de un note_item por medio de datos en crudo.
# def note_item_createv(request):
#
#     inital_data = {
#         'title': 'My title'
#     }
#
#     form = NoteItemForm(request.POST or None, initial= inital_data)
#     if form.is_valid():
#         form.save()
#         return redirect('../' + str(Note_item.objects.latest('id').id) + '/details/')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'note_item/note_item_create.html', context)

# OBSOLETO - Contiene manejo de la generación de la lista de note_item existentes en la base de datos
# por medio de datos en crudo.
'''
def note_item_listv(request):

    queryset = Note_item.objects.all()

    context = {
        'note_item_list': queryset
    }
    return render(request, "note_item/my_notes.html", context)
'''

# OBSOLETO - Contiene manejo de la eliminación de un note_item por medio de datos en crudo.
# def note_item_delete(request, id_req):
#     print('Entrando')
#     object = get_object_or_404(Note_item, id=id_req)
#     #POST request
#     if request.method == "POST":
#         #confirming delete
#         print('Por POST')
#         object.delete()
#         return redirect('../../../')
#
#
#     context = {
#         'obj': object
#     }
#     return render(request, 'note_item/note_item_delete.html', context)

# OBSOLETO - Contiene manejo del formulario para la edición de un note_item por medio de datos en crudo.
# def note_item_editv(request, id_req):
#     obj = get_object_or_404(Note_item, id=id_req)
#     form = NoteItemForm(request.POST or None, instance= obj)
#     '''
#         try:
#         obj = Note_item.objects.get(id=id_req)
#         except Note_item.DoesNotExist:
#         raise Http404
#     '''
#     if form.is_valid():
#         print('Valido')
#         form.save()
#         return redirect('../../' + str(id_req) + '/details/')
#     else:
#         print('No valido')
#
#     context = {
#         'form': form,
#         'id': id_req
#     }
#     return render(request, 'note_item/note_item_edit.html', context)

# OBSOLETO - Contiene manejo para acceder al último note_item de la base de datos ordenando por id,
# por medio de datos en crudo.
'''
def note_item_lastCreated(request):
    last_note = Note_item.objects.latest('id')

    context = {
        'object': last_note
    }

    return render(request, 'note_item/note_item_detail.html', context)
'''

# OBSOLETO - Contiene manejo de la generación de detalles de un note_item por medio de datos en crudo.
'''
def note_item_detailv(request, id_req):
    #com
    Vista detallada para un note item
    :param request: request para el HttpResponse
    :return: HttpResponse para la visualización de dicho note item
    #com
    try:
        note = Note_item.objects.get(id=id_req)
    except Note_item.DoesNotExist:
        raise Http404
    #note = get_object_or_404(Note_item, id=id_req)

    #com
    context = {
        'title': note.title,
        'description': note.description,
        'summary': note.summary,
        'created_date': '/'.join((str(note.created.day), str(note.created.month), str(note.created.year))),
        'created_time': ':'.join((str(note.created.hour), str(note.created.minute))),
        'modified_date': '/'.join((str(note.modified.day), str(note.modified.month), str(note.modified.year))),
        'modified_time': ':'.join((str(note.modified.hour), str(note.modified.minute)))
    }
    #com
    context = {
        'object': note
    }
    return render(request, 'note_item/note_item_detail.html', context)
'''
