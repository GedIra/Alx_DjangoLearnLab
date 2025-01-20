from django.urls import path, include
from .views import ( PostsViewset, CommentSViewset
                )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostsViewset, basename='post')
router.register(r'comments', CommentSViewset, basename='comment')


urlpatterns = [
  path('', include(router.urls)),
]


