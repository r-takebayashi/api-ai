from django.conf.urls import url

from . import views

urlpatterns = [
#:w    url(r'^$', views.index, name='index'),
#    url(r'^forms/$', views.index, name='index'),
    url(r'^forms/$', views.question_forms, name='hello_forms'),
]
