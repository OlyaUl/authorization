from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login_view/$', views.login_view, name='login_view'),
    url(r'^register_view/$', views.register_view, name='register_view'),
    #url(r'^register_view/$', views.UserFormView.as_view(), name='register_view'),

    url(r'^$', views.index, name='index'),

]