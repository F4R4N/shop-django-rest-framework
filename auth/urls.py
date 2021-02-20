from django.urls import path
from auth.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, UpdateUserImageView, DeleteProfile
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('change_image/<int:pk>/', UpdateUserImageView.as_view(), name='auth_image'),
    path('delete_profile/<int:pk>/', DeleteProfile.as_view(), name='auth_delete_profile')
]
