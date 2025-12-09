
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls'), name='users'),
    path('api/v1/papers/', include('papers.urls'), name='papers'),
    path('api/v1/ai_chat/', include('ai_chats.urls'), name='ai_chats'),
]
