from django.urls import path
from .views import JobsListView, JobDetailView

urlpatterns = [
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('', JobsListView.as_view(), name='home'),
]