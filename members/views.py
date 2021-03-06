from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .forms import UserCreateForm, UserUpdateForm, CustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from mainapp.models import Article, Comment
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Customer
 

def register(request):
    error = ''
    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            form.save() # если данные из формы валидны то сохраняем
            username = request.POST.get('username') # имя пользователя для аутентификаци
            password = request.POST.get('password1') # пороль пользователя для аутентификаци
            user = authenticate(request, username = username, password = password)

            if user is not None: # тут проверяем если не авторизован то тут же авторизуем 
                login(request, user)
                return HttpResponseRedirect('/user/image' + str(request.user.id)) 

        else:
            error = 'Логин бос емес немесе құпия сөздер сәйкес емес!'
            context = {
                'register_form':form,
                'message':error,
            }
            return render(request, 'members/register.html', context)

    else:
        form = UserCreateForm()
  
    return render(request, 'members/register.html', {'register_form':form})


def auth(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/user/profile/' + str(request.user.id))
        else:
            error = 'Қолданушы атауы немесе құпия сөз дұрыс емес!'
            return render(request, 'members/auth.html', {'error':error})
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
        context['profile'] = Customer.objects.all()
        context['comments'] = Comment.objects.all()
        # context['all_friend_requests'] = Friend_Request.objects.all()
        return context


class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'members/profile_update.html'
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')


def CustomeView(request, pk):
     
    if request.method == 'POST':
        news_form = CustomerForm(request.POST)
        
        # self.instance.author = self.request.user
        if news_form.is_valid():
            news_form = news_form.save(commit=False)
            news_form.user = request.user
            news_form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Дұрыс толтырылмады!')

    news_form = CustomerForm()
    data = {
        'form':news_form
    }
     
    return render(request, 'members/user_pic.html', data)


class CustomeUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'members/custome_update.html'
     
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')