from django.http import HttpResponse
from django.shortcuts import render

'''
Pages HttpResponse
'''
def homepage_view(request,*args, **kwargs):
    print('Logged as: {}'.format(request.user))
    if request.user.is_authenticated:
        return render(request, "home.html", {})
    return render(request, "login.html", {})

def notes_view(request, *args, **kwargs):
    note_context = {
        "info": "Here will appear all your saved notes",
        "list": [11, 22, 33, 44, 55, 66],
        "my_title": 'welcome to your notes',
        "my_html": '<h1>This is html from views</h1>'
    }

    return render(request, "my_notes.html", note_context)