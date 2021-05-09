from django.urls import path
from . import views 


urlpatterns = [
    path('', views.MainView.as_view(), name = 'home'),
    path('add/', views.ArticleAddView , name = 'add'),
    path('add/post', views.PostAddView , name = 'add_post'),
    path('object-<int:pk>', views.MainDetailView.as_view(), name = 'details'),
    path('delete-<int:pk>', views.ArticleDeleteView.as_view(), name = 'delete'),
    path('update-<int:pk>', views.ArticleUpdateView.as_view(), name = 'update'),
]
