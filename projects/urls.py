from django.urls import path
from projects.views import *

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]