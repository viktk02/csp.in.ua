from django.urls import path
from posts.views import *

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]