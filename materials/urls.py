from django.urls import path

from main.apps import MainConfig
from materials.views import MaterialCreateView

app_name = MainConfig.name

urlpatterns = [
    path('create/', MaterialCreateView.as_view(), name='create'),
    # path('', ...., name='list'),
    # path('view/<int:pk>/', ...., name='view'),
    # path('edit/<int:pk>/', ...., name='edit'),
    # path('delite/<int:pk>/', ...., name='delite')
]
