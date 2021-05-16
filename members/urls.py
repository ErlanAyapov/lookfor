from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout, name = 'logout'),
    path('auth/', views.auth, name = 'auth'),
    path('profile/<int:pk>', views.UserProfileView.as_view(), name = 'profile'),
    path('update/<int:pk>', views.UserProfileUpdateView.as_view(), name = 'profile_update'),
    path('pic/<int:pk>', views.CustomeView, name = 'pic_update'),
    path('custome-update/<int:pk>', views.CustomeUpdateView.as_view(), name = 'custome_update'),
]
