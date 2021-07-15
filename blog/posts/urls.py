from django.urls import path

from posts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name="logout"),
    path('about/', views.about, name='about'),
    path('post/', views.PostList.as_view(), name='post'),
    path('post/create/', views.PostCreate.as_view(), name='post_create_form'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdate.as_view(), name='post_create_form'),
    path('product/', views.ProductList.as_view(), name='product'),
    path('product/create/', views.ProductCreate.as_view(), name='product_create_form'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('product/<int:pk>/edit/', views.ProductUpdate.as_view(), name='product_create_form'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
