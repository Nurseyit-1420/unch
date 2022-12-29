from django.urls import path
from .views import PostListViev, PostCreateView,PostDetailView


urlpatterns = [
    path('',PostListViev.as_view(), name ='post-list'),
    path('create/',PostCreateView.as_view(), name='create'),
    path('post/<int:pk>',PostDetailView.as_view(), name='post-detail' )
]