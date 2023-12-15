from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from accounts.viewsets import UserViweSet, UserMeViewSet

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('', UserViweSet.as_view({'post': 'create'}), name='user'),
    path('me/', UserMeViewSet.as_view({'get': 'retrieve'}), name='user_me')
]
