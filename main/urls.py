from django.urls import path

from main.apps import MainConfig
from main.views import StudentListView
app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index')
]
