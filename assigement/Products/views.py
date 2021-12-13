from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,ListView
from ..User.models import Post

# Create your views here.

class create_mod(CreateView):
    model = Post
    fields = ('__all__')
    template_name = 'form.html'
    success_url = '/'



class list(ListView):
    model = Post
    template_name = "form.html"
    context_object_name = "lis"

#@login_required(login_url='/login')

#def posting(request):
 #   form =
