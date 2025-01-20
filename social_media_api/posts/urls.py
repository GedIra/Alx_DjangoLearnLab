from django.urls import path
from .views import ( PostlistCreateAPIView, PostRetrieveUpdateDeleteAPIView,
                    CommentListCreateapiView, CommentRetrieveUpdateDeleteAPIView,
                )


urlpatterns = [
  path('posts/', PostlistCreateAPIView.as_view(), name='posts'),
  path('post/<int:pk>/', PostRetrieveUpdateDeleteAPIView.as_view(), name='post-detail'),
  path('comments/', CommentListCreateapiView.as_view(), name='comments'),
  path('post/comment/<int:pk>/', CommentRetrieveUpdateDeleteAPIView.as_view(), name='comment-detail')
]
