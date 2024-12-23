from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='user-list')
router.register(r'comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('follow/', FollowListCreateAPIView.as_view(), name='follow_list'),
    path('post/', PostListCreateAPIView.as_view(), name='post'),
    path('post_like/', PostLikeListAPIView.as_view(), name='post_like'),
    path('comment_like/', CommentLikeListApiVIew.as_view(), name='comment_like'),
    path('story/', StoryListCreateAPIView.as_view(), name='story'),
    path('saved/', SavedListApiVIew.as_view(), name='saved'),
    path('save_item/', SaveItemListApiVIew.as_view(), name='save_item'),

]
