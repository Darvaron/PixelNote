from django.shortcuts import render
from .models import Note_item
from .forms import NoteItemForm

def note_item_createv(request):

    if request.method == 'POST':
        my_new_title = request.POST.get('title')
        # Note_item.objects.create(title= my_new_title)
        print(my_new_title)

    context = {
    }
    return render(request, 'note_item/note_item_create.html', context)


'''
def note_item_createv(request):
    form = NoteItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NoteItemForm()

    context = {
        'form': form
    }
    return render(request, 'note_item/note_item_create.html', context)
'''
def note_item_lastCreated(request):
    last_note = Note_item.objects.latest('id')

    context = {
        'object': last_note
    }

    return render(request, 'note_item/note_item_detail.html', context)

def note_item_detailv(request, id_req=1):
    '''
    Vista detallada para un note item
    :param request: request para el HttpResponse
    :return: HttpResponse para la visualización de dicho note item
    '''
    note = Note_item.objects.get(id=id_req)

    '''
    context = {
        'title': note.title,
        'description': note.description,
        'summary': note.summary,
        'created_date': '/'.join((str(note.created.day), str(note.created.month), str(note.created.year))),
        'created_time': ':'.join((str(note.created.hour), str(note.created.minute))),
        'modified_date': '/'.join((str(note.modified.day), str(note.modified.month), str(note.modified.year))),
        'modified_time': ':'.join((str(note.modified.hour), str(note.modified.minute)))
    }
    '''
    context = {
        'object': note
    }
    return render(request, 'note_item/note_item_detail.html', context)
