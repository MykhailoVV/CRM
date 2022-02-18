from django.urls import path
from .views import JobsListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView

urlpatterns = [
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('job/<int:pk>/edit/', JobUpdateView.as_view(), name='job_edit'),
    path('job/new/', JobCreateView.as_view(), name='job_new'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('', JobsListView.as_view(), name='home'),
]