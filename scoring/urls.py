from django.urls import path, include
from . import views

app_name = 'scoring'

urlpatterns = [
    path('/kakaotalk/<int:step>/<int:result>',
         views.KakaoView.as_view(), name='index'),
]
