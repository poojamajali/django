from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Job
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class JobsCreateView(LoginRequiredMixin, CreateView):
    model= Job
    fields=['Job_role','qualification','specialisation','location','salary','date']
    def form_valid(self,form):
        return super().form_valid(form)

   

class JobListView(ListView):
    model= Job
    template_name = 'jobs/home.html'
    context_object_name='jobs'
    # order new to old
    ordering=['-date']

class JobDetailView(DetailView):
    model= Job



def hubli(request):

    context={
        'hublijobs':Job.objects.filter(location='Hubli',salary=50000),
        'size':len(Job.objects.filter(location='Hubli',salary=50000))
        
    }
    return render(request,'jobs/count.html',context)