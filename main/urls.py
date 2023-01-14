from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('demand', views.demand, name='demand'),
    path('geography', views.geography, name='geography'),
    path('vacancies', views.vacancies, name='vacancies'),
    path('skills', views.skills, name='skills'),
]
