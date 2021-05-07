from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout, name = 'logout'),
    path('auth/', views.auth, name = 'auth'),
    path('profile/<int:pk>', views.UserProfileView.as_view(), name = 'profile'),

    path(r'dialogs/', views.DialogsView.as_view(), name='dialogs'),
	path(r'^dialogs/create/(?P<user_id>\d+)/$', views.CreateDialogView.as_view(), name='create_dialog'),
	path(r'^dialogs/(?P<chat_id>\d+)/$', views.MessagesView.as_view(), name='messages'),

]
