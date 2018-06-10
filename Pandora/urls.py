from django.conf.urls import url
from Pandora.views import index

urlpatterns = [
    url(r'^', index),
]
