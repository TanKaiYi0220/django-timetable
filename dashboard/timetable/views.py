from django.conf.urls import url
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

import timetable
from .models import User, Timetable, TimetableRow, TimetableElement
from .forms import CustomUserCreationForm, TimetableRowCreationForm, TimetableElementUpdateForm
# Create your views here.
def home(request):
    context = {}
    return render(request, 'base/home.html', context)

# def timetablePage(request):
#     header = ['Time', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

#     class timetableRow():
#         def __init__(self, time):
#             self.time = time
#             self.elements = ['None'] * 7

#     class timetableElement():
#         def __init__(self, activity):
#             self.activity = activity
#             self.tag = None

#         def context(self):
#             return self.activity + "," + self.tag.label + "," + self.tag.color

#     class timetableTag():
#         def __init__(self, label, color):
#             self.label = label
#             self.color = color

#     timetableRows = [timetableRow("8:00-12:00"), timetableRow("12:00-16:00")]
#     study_element = timetableElement('Study')
#     play_element = timetableElement('Play')
#     education_tag = timetableTag('Education', 'red')
#     entertainment_tag = timetableTag('Entertainment', 'green')

#     study_element.tag = education_tag
#     play_element.tag = entertainment_tag

#     timetableRows[0].elements[0] = study_element
#     timetableRows[0].elements[2] = study_element
#     timetableRows[1].elements[0] = play_element

#     context = {'header': header, 'timetableRows': timetableRows}
#     return render(request, 'base/timetable.html', context)

def timetablePage(request, pk):
    form = TimetableRowCreationForm()

    header = ['Time', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    user = User.objects.get(id=pk)
    timetable = user.timetable_set.all()[0]
    timetableRows = timetable.timetablerow_set.all()

    if request.method == 'POST':
        timetableRow = TimetableRow.objects.create(
            timetable=timetable,
            start=request.POST.get('start'),
            end=request.POST.get('end')
        )
        for i in range(1, 8):
            TimetableElement.objects.create(
                timetable=timetable,
                row=timetableRow,
                day=i,
                body='None',
            )
        return redirect('timetable', pk=pk)


    context = {'header': header, 'user': user, 'timetable': timetable, 'timetableRows': timetableRows, 'form': form}

    return render(request, 'base/timetable.html', context)

def deleteTimetableRow(request, pk, tpk):
    timetableRow = TimetableRow.objects.get(id=pk)

    if request.method == 'POST':
        timetableRow.delete()
        return redirect('/timetable/'+tpk)
    
    return render(request, 'base/deleteTimetableRow.html', {'obj': timetableRow})

def updateTimetableElement(request, pk, tpk):
    timetableElement = TimetableElement.objects.get(id=pk)
    form = TimetableElementUpdateForm()

    if request.method == 'POST':
        print('*'*10, timetableElement.body, request.POST.get('body'), tpk)
        timetableElement.body = request.POST.get('body')
        timetableElement.save()
        return redirect('/timetable/'+tpk)

    return render(request, 'base/updateTimetableElement.html', {'obj': timetableElement, 'form': form})

def loginPage(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            print("Error")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Error")

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            Timetable.objects.create(
                host=user,
                name='Automatically Timetable'
            )
            login(request, user)
            return redirect('home')
        else:
            print("Error")

    context = {'form': form}
    return render(request, 'base/login_register.html', context)