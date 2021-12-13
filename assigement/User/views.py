

# Create your views here.
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.views.generic import CreateView,ListView
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import UserForm

from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

# Create your views here.



class create_mod(LoginRequiredMixin,CreateView):
    model = Post
    fields = ('__all__')
    template_name = 'Post.html'
    success_url = '/list'



class list(ListView):
    model = Post
    template_name = "list.html"
    context_object_name = "lis"

def fun(request):
    return render(request,("index.html"))


# def signup(request):
#     form1=signup_form()
#     context={
#         'form1':form1
#     }
#     if request.method == 'POST':
#         user=signup_form(request.POST)
#         if user.is_valid():
#          user.save()
#     return HttpResponse('Usersave')
#     return render(request,'signup.html',context=context)
#

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()


    return render(request, 'register.html', {'form': form})



