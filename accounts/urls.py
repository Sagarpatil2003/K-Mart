from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login_view"),
    path('logout/', views.logout_view, name='logout_view'),
    path('create_account/', views.RegistrationView.as_view(), name='user_registrationform'),
    path('profile/', views.ProfileView.as_view(), name='ProfileView'),

    
    # Password Update URLs
    path('password_update/', views.password_update_view, name='password_update'),
]
