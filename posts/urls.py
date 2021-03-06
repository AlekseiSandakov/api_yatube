from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet


router_V1 = DefaultRouter()
router_V1.register(
    'posts',
    PostViewSet,
    basename='posts',
)
router_V1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_V1.urls)),
]
