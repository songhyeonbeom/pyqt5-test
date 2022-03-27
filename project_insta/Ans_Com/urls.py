from django.urls import path
from Ans_Com import views


app_name = 'Ans_Com'
urlpatterns = [
    path('answer/create/<int:photo_id>/', views.answer_create, name='answer_create'),


]