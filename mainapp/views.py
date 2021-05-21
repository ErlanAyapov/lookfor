from django.shortcuts import render
from .models import Article, Comment
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .forms import ArticleForm, PostAdd, CommentForm, CommentUpdateForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
# def MainView(request):
# 	return render(request, 'index/index.html')

class MainView(ListView):
	model = Article
	template_name = 'index/index.html'
	ordering = '-date'

	def get_context_data(self, **kwargs):
		context = super(MainView, self).get_context_data(**kwargs)
		context['comment'] = Comment.objects.all()
		return context

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

class ArticlePostUpdate(UpdateView):
	model = Article
	form_class = PostAdd
	template_name = 'index/post_update.html'
	
	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/')


def CommentAddView(request):
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		
		# self.instance.author = self.request.user
		if comment_form.is_valid():
			comment_form = comment_form.save(commit=False)
			comment_form.author = request.user
			comment_form.category = 'Пост'
			comment_form.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('Дұрыс толтырылмады!')

	comment_form = CommentForm()
	data = {
		'comment_form':comment_form,
		 
	}
	return render(request, 'index/comment.html', data)

class CommentUpdateView(UpdateView):
	model = Comment
	form_class = CommentUpdateForm
	template_name = 'index/comment_update.html'

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/')

# class CommentUpdateView(DeleteView):
# 	model = Comment
# 	template_name = 'index/comment_update.html'
# 	success_url = reverse_lazy('home')