from django.urls import path, include
from . import views

app_name = 'scoring'

urlpatterns = [
    path('kakaotalk/1/r', views.k1r.as_view(), name='index'),
    path('kakaotalk/1/w', views.k1w.as_view(), name='index'),
]
