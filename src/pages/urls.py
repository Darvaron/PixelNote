from django.urls import path
from .views import (
    home_view
)

'''
Descripción: Manejo de la página de la URL de la página de inicio
'''

# Nombre correspondiente a la aplicación para identificación de URLs
app_name = 'pages'

# URLs asociadas
urlpatterns = [
    path('', home_view.as_view(), name='home')
]
