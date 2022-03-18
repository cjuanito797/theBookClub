from django.contrib.auth import views as auth_views
from django.urls import path, re_path


from . import views
app_name = 'accounts'

urlpatterns = [
    re_path (r'^customerView/$', views.customerView, name='customerView'),
    path('register/', views.registration_view.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('bookshelf/' ,views.myBookShelf, name='myBookShelf'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('addBook/', views.addBook, name='addBook'),


]