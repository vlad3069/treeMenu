from django.urls import path

from djangoApp import views

app_name = 'djangoApp'

urlpatterns = [
    path('<str:menu_name>/', views.draw_menu, name='draw_menu'),
]
