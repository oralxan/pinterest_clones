from django.urls import path
from pinterest.views import post_list,home_page,post_detail,post_create,post_edit,post_delete,my_post,signup,LoginPage



urlpatterns = [
    path('', home_page, name='home_page'),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/new/', post_create,name='post_create'),
    path('posts/update/<int:pk>/', post_edit,name='post_edit'),
    path('posts/delete/<int:pk>/', post_delete,name='post_delete'),
    path('profile/',my_post,name='my_post'),
    path('signup/',signup,name='signup'),
    path('login/',LoginPage,name='LoginPage'),

]

    





