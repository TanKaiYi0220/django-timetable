from django.contrib import admin
from .models import Timetable, TimetableRow, TimetableElement, User

# Register your models here.
admin.site.register(User)
admin.site.register(Timetable)
admin.site.register(TimetableRow)
admin.site.register(TimetableElement)