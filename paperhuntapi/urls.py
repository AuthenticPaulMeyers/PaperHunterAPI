
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'), name='users'),
    path('papers/', include('papers.urls'), name='papers'),
    path('ai_chats/', include('ai_chats.urls'), name='ai_chats'),

    path('api-auth/', include('rest_framework.urls')),
]
