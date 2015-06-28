from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'myapp/', views.homepage, name='home'),
    url(r'^list$', views.list_employee, name='list_employee'),
    url(r'^create$', views.create_employee, name='create_employee'),
    url(r'^save$', views.save_employee, name='save_employee'),
    url(r'^edit/(?P<pk>\d+)$', views.edit_employee, name='edit_employee'),
    url(r'^update$', views.update_employee, name='update_employee'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_employee, name='delete_employee'),
]