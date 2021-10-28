from django.urls import path
from .views import like_post, post_view

app_name = 'quickstart'

urlpatterns = [
    path('', post_view, name='post_list'),
    path('like/', like_post, name='like_post'),
    
]
