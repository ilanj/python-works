from django.conf.urls import url
from . import views

urlPatterns=[
    url('myapp',views.index, name='index')
]