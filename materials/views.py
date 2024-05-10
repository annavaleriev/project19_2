from django.shortcuts import render
from django.views.generic import CreateView

from materials.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ['title', 'body']


