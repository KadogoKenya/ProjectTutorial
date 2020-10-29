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
from .forms import NewTutorialForm


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
    template_name = 'tutorial/index.html'
    context_object_name = 'tutorials'
    ordering = ['-Published']

def index(request):

    tutorials = Tutorial.get_all_images()
    print(tutorials)
    context={
        'tutorials':tutorials,
    }

    return redirect(request,'index.html', context)


class TutorialDetailView(DetailView):
    model = Tutorial

class TutorialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tutorial
    fields = ['title', 'description', 'image', 'content','Author','Published','Unpublished']
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
   
    def test_func(self):
        tutorial = self.get_object(Tutorial)
        if self.request.user == tutorial.user:
            return True
        return False

class TutorialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tutorial
    success_url = '/tutorialproject'
    

    def test_func(self):
        tutorial = self.get_object()
        if self.request.user == tutorial.user:
            return True
        return False

def search_results(request):

    if 'tutorial' in request.GET and request.GET["tutorial"]:
        search_term = request.GET.get("tutorial")
        searched_tutorials = Tutorial.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'tutorial/search.html',{"message":message,"tutorial": searched_tutorial})

    else:
        message = "You haven't searched for any term"
        return render(request, 'tutorial/search.html',{"message":message})


def new_tutorial(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewTutorialForm(request.POST, request.FILES)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.Author = current_user
            tutorial.save()
        return redirect('NewsToday')

    else:
        form = NewTutorialForm()
    return render(request, 'new_tutorial.html', {"form": form})