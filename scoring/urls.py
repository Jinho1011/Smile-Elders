from django.urls import path, include
from . import views

app_name = 'scoring'

urlpatterns = [
    path('kakaotalk/<int:step>/<int:result>',
         views.KakaotalkMessageView.as_view(), name='index'),
    path('kakaotalk/result',
         views.KakaotalkMessageResultView.as_view(), name='index'),
]
