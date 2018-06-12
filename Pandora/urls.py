from django.conf.urls import url
from Pandora.views import index,tools_test

urlpatterns = [
    url(r'^', index),
    url(r'^tools_test/$', tools_test, name='tools_test'),
]
