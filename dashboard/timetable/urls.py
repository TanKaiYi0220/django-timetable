from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('timetable/<str:pk>/', views.timetablePage, name='timetable'),
    path('timetable/deleteRow/<str:pk> <str:tpk>', views.deleteTimetableRow, name='delete-row'),
    path('timetable/updateElement/<str:pk> <str:tpk>', views.updateTimetableElement, name='update-element'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
]
