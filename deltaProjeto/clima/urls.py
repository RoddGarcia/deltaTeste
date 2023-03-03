from django.urls import path
from .views import index, editar, deletar

urlpatterns = [
    path('', index, name='index'),
    path('<str:estadoSelecionado>/', index, name='index'),
    path('editar/', editar, name='editar'),
    path('deletar/<int:id>/', deletar, name='deletar')
]
