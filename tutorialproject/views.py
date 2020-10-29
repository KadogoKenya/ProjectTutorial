from django.shortcuts import render,redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tutorial
from django.views.generic import  ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from users.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'tutorial/index.html')

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class TutorialCreateView(LoginRequiredMixin,CreateView):
    
    model = Tutorial
    fields = ['title', 'description', 'image', 'content','Author','pub_date','updated_date','Published','Unpublished']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TutorialListView(ListView):
    model = Tutorial
    template_name = 'tutorial/tutorialpoint.html'
    context_object_name = 'tutorials'
    ordering = ['-submitted']

class TutorialDetailView(DetailView):
    model = Tutorial