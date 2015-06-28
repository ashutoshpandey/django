from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^myapp/list$', views.list_employee, name='list_employee'),
    url(r'^myapp/create$', views.create_employee, name='create_employee'),
    url(r'^myapp/save$', views.save_employee, name='save_employee'),
    url(r'^myapp/edit/(?P<pk>\d+)$', views.edit_employee, name='edit_employee'),
    url(r'^myapp/update$', views.update_employee, name='update_employee'),
    url(r'^myapp/delete/(?P<pk>\d+)$', views.delete_employee, name='delete_employee'),
    url(r'myapp/', views.homepage, name='home'),
]