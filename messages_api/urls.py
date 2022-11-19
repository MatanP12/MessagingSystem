from django.urls import path

from .views import (
    MessageListView,
    NewMessageListView,
    MessageDetailApiView
)

urlpatterns = [
    path('', MessageListView.as_view()),
    path('new', NewMessageListView.as_view()),
    path('<int:message_id>', MessageDetailApiView.as_view()),
]