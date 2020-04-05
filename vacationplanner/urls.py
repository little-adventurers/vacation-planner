from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from vacationplanner import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^vacations/(?P<pk>\d+)/$', views.vacation_itineraries, name='vacation_itineraries'),
    url(r'^vacations/(?P<pk>\d+)/', views.Vacation, name='vacation_itineraries'),
    url(r'^admin/', admin.site.urls),
]