from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .forms import UserCreateForm #, UserUpdateForm, UserCustomerUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from mainapp.models import Article
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Chat


def register(request):
 	if request.method == 'POST':
 		form = UserCreateForm(request.POST)

 		if form.is_valid():
 			form.save()
 			return redirect('auth')

 		else:
 			return HttpResponse("<h1 style = 'text-align: center;'>Логин бос емес немесе құпия сөз құптамасы дұрыс емес</h1>")

 	else:
 		form = UserCreateForm()
  
 	return render(request, 'members/register.html', {'register_form':form})


def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("<h1 style = 'text-align: center;'>Қолданушы атауы немесе құпия сөз дұрыс емес!</h1>")
    return render(request, 'members/auth.html')


def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')

class UserProfileView(DetailView):
    queryset = User.objects.all()
    template_name = 'members/profile.html'


    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['news'] = Article.objects.order_by('-date')
        # context['all_friend_requests'] = Friend_Request.objects.all()
        return context

