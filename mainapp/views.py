from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .forms import ArticleForm, PostAdd
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
# def MainView(request):
# 	return render(request, 'index/index.html')

class MainView(ListView):
	model = Article
	template_name = 'index/index.html'
	ordering = '-date'


class MainDetailView(DetailView):
	model = Article
	template_name = 'index/article_detail.html'

def ArticleAddView(request):
	error = ''
	if request.method == 'POST':
		news_form = ArticleForm(request.POST)
		
		# self.instance.author = self.request.user
		if news_form.is_valid():
			news_form = news_form.save(commit=False)
			news_form.author = request.user
			news_form.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('Дұрыс толтырылмады!')

	news_form = ArticleForm()
	data = {
		'form':news_form,
		'error':error,
		'range_b': range(1, 32),
        'range_y': range(2006, 1930, -1)
	}
	return render(request, 'index/article_add.html', data)

def PostAddView(request):
	error = ''
	if request.method == 'POST':
		news_form = PostAdd(request.POST)
		
		# self.instance.author = self.request.user
		if news_form.is_valid():
			news_form = news_form.save(commit=False)
			news_form.author = request.user
			news_form.category = 'Пост'
			news_form.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('Дұрыс толтырылмады!')

	news_form = PostAdd()
	data = {
		'post_form':news_form,
		 
	}
	return render(request, 'index/add_post.html', data)


class ArticleDeleteView(DeleteView):
	model = Article
	template_name = 'index/article_delete.html'
	success_url = reverse_lazy('home')


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'index/article_update.html'
    # fields = ['title', 'slug', 'body', 'image']
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')