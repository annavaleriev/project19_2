import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from materials.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ['title', 'body']
    success_url = reverse_lazy("many:index")


