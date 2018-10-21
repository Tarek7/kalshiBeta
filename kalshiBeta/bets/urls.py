from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<int:question_id>/', views.Question, name='question'),
    path('<int:question_id>/myBets/', views.MyBets, name='myBets'),
]
