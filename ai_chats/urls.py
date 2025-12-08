from django.urls import path
from . import views

# Create URL patterns here.
app_name = 'ai_chats'
urlpatterns = [
    path('', views.index, name='index'),
]