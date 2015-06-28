from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'myapp/', views.homepage, name='home'),
]