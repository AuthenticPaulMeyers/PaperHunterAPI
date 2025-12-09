from django.urls import path
from . import views

# Create URL patterns here.
app_name = 'ai_chats'
urlpatterns = [
    path('sessions/<int:paper_id>/', views.new_chat_session, name='new_chat_session'),
    path('sessions/', views.show_chats, name='show_chats'),
    path('sessions/<int:session_id>/messages/', views.show_message_history, name='show_message_history'),
    path('sessions/<int:session_id>/ask/', views.user_query, name='user_query'),
]