from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]