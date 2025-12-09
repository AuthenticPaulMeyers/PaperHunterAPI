
from django.urls import path
from . import views

# Create URL patterns here.
app_name = 'papers'     
urlpatterns = [
      path('', views.index, name='index'),
]