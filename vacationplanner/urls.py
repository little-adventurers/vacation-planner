from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from vacationplanner import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]