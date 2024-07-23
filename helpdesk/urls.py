from django.urls import path
from . import views

urlpatterns = [
    path("", views.problems, name="problems"),
    path("problem/<str:id>", views.indproblem, name="problem"),
    path("home/", views.home, name="home"),
    path("form/",views.model_form),
]
