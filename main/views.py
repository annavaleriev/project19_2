from django.shortcuts import render
from django.views.generic import ListView

from main.models import Student


# Create your views here.

# def index(request):
#     student_list = Student.objects.all()
#     context = {
#         'object_list': student_list
#     }
#     return render(request, 'main/index.html', context)

class StudentListView(ListView):
    model = Student
    template_name = 'main/index.html'



# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}) : {message}')
#
#     return render(request, 'main/index.html')
