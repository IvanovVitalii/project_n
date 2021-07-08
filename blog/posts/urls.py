from django.conf.global_settings import LOGOUT_REDIRECT_URL
from django.conf.urls import url
from django.contrib.auth.views import LogoutView

from django.urls import path

from posts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('home/', views.PostList.as_view(), name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('create/', views.create_post, name='post_create_form'),
    path('home/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('home/<int:pk>/edit/', views.post_edit, name='post_create_form'),
]
