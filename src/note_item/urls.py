from django.urls import path
from .views import (
    note_item_create_view,
    note_item_edit_view,
    note_item_delete_view,
    note_item_list_view,
    note_item_detail_view
)

'''
Descripción: Manejo de las URLs asociadas a note_item
'''

# Nombre correspondiente de la aplicación para identificación de URLs
app_name = "notes"

# URLs asociadas
urlpatterns = [
    path('', note_item_list_view.as_view(), name='notes'),
    path('create/', note_item_create_view.as_view(), name='create'),
    path('<int:id_req>/details/', note_item_detail_view.as_view(), name='details'),
    path('<int:id_req>/edit/', note_item_edit_view.as_view(), name='edit'),
    path('<int:id_req>/delete/', note_item_delete_view.as_view(), name='delete')
]
