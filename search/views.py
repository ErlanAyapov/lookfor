from django.shortcuts import render
from django.views.generic import ListView
from mainapp.models import Article
from simple_search import search_filter


def search(request):
	pass
 
class SearchResultsView(ListView):
    model = Article
    template_name = 'search/search_results.html'
    ordering = '-date'

    def get_queryset(self):
        search_fields = ['first_name', 'last_name', 'third_name', 'fourth_name', 'fiveth_name', 'sixth_name', 'seventh_name']
        query = self.request.GET.get('q')
        results = Article.objects.filter(search_filter(search_fields, query))

        return results
