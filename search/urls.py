from django.urls import path
from . import views
# from .views import SearchResultsView


urlpatterns = [
	path('', views.SearchResultsView.as_view(), name = 'search'),
]
