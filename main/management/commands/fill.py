from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'first_name': "Аня", 'last_name': "Иваенова"},
            {'first_name': "Вова", 'last_name': "Петров"},
            {'first_name': "Маша", 'last_name': "Кац"},
            {'first_name': "Миша", 'last_name': "Фролов"},
            {'first_name': "Мван", 'last_name': "Го"}
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )
        Student.objects.bulk_create(students_for_create)
