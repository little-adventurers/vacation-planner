from django.urls import include, path
from vacationplanner import views

urlpatterns = [
    path("", views.home, name="home"),
]