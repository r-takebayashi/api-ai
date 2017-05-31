from django.conf.urls import url

from . import views
from django.conf import settings
import django

urlpatterns = [
#:w    url(r'^$', views.index, name='index'),
#    url(r'^forms/$', views.index, name='index'),
    url(r'^forms/$', views.question_forms, name='hello_forms'),
#    url(r'^static_site/(?P<path>.*)$',django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
]
