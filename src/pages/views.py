from django.shortcuts import render
from django.views import View

'''
Descripción: Manejo de las páginas asociadas a /home/ y //
'''


class home_view(View):
    '''
    Genera la carga de la página asociada a /home/ si el usuario se encuentra registrado,
    de lo contrario lo redirige a la página de login
    '''
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):  # El nombre de la función puede ser cambiado a POST si se usa dicho método
        # método GET
        print('Inició sesión como: {}'.format(request.user))
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        return render(request, "login.html", {})

# OBSOLETO - Contiene manejo de la página de inicio por medio de datos en crudo.
# def homepage_view(request,*args, **kwargs):
#     print('Logged as: {}'.format(request.user))
#     if request.user.is_authenticated:
#         return render(request, "home.html", {})
#     return render(request, "login.html", {})

# OBSOLETO - Contiene manejo de página de prueba por medio de datos en crudo.
# def notes_view(request, *args, **kwargs):
#     note_context = {
#         "info": "Here will appear all your saved notes",
#         "list": [11, 22, 33, 44, 55, 66],
#         "my_title": 'welcome to your notes',
#         "my_html": '<h1>This is html from views</h1>'
#     }
#
#     return render(request, "my_notes.html", note_context)
