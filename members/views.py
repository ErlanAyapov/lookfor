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
from index.models import Article
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


class DialogsView(DetailView):
    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])
        return render(request, 'members/messages.html', {'user_profile': request.user, 'chats': chats})


class MessagesView(DetailView):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        return render(
            request,
            'members/create_message.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat_id}))



class CreateDialogView(CreateView):
    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id], type=Chat.DIALOG).annotate(c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat.id}))