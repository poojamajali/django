from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  
    path('jobs/new',views.JobsCreateView.as_view(),name='job-create'),
    path('post/<int:pk>',views.JobDetailView.as_view(),name='job-detail'),
    path('home/', views.JobListView.as_view(),name='job-home'),
    path('number/',views.hubli,name='count')

]
