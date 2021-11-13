from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.enums import IntegerChoices
# Create your models here.

class User(AbstractUser):
    pass

# class Tag(models.Model):
#     pass

class Timetable(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TimetableRow(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, null=True)
    start = models.TimeField(null=True)
    end = models.TimeField(null=True)

    class Meta:
        ordering = ['start', 'end']

    def __str__(self):
        return str(self.start) + ' - ' + str(self.end)

    def get_all_elements(self):
        elements = [None] * 7
        timetableE = self.timetableelement_set.all()
        for e in timetableE:
            elements[e.day-1] = e
        return elements


class TimetableElement(models.Model):
    class Day(models.IntegerChoices):
        MON = 1
        TUE = 2
        WED = 3
        THU = 4
        FRI = 5
        SAT = 6
        SUN = 7

    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, null=True)
    row = models.ForeignKey(TimetableRow, on_delete=models.CASCADE)
    day = models.IntegerField(choices=Day.choices, default=Day.MON)
    body = models.CharField(max_length=100)

    class Meta:
        ordering = ['day']

    def __str__(self):
        return self.body

