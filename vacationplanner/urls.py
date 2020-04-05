from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from vacationplanner import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^itinerary/(?P<pk>\d+)/$', views.Itinerary, name='vacation_itinerary'),
    url(r'^admin/', admin.site.urls),
]