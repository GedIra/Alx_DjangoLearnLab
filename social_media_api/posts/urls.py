from django.urls import path
from .views import ( PostlistCreateAPIView, PostRetrieveUpdateDeleteAPIView,
                    CommentListCreateapiView, CommentRetrieveUpdateDeleteAPIView,
                )


urlpatterns = [
  path('api/posts/', PostlistCreateAPIView.as_view(), name='posts'),
  path('api/post/<int:pk>/', PostRetrieveUpdateDeleteAPIView.as_view(), name='post-detail'),
  path('api/comments/', CommentListCreateapiView.as_view(), name='comments'),
  path('api/post/comment/<int:pk>/', CommentRetrieveUpdateDeleteAPIView.as_view(), name='comment-detail')
]
