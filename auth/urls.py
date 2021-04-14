from django.urls import path
from auth.views import (
    RegisterView, ChangePasswordView, UpdateProfileView, LogoutView,
    UpdateUserImageView, DeleteProfileView, ResetPasswordView,
    ValidateConfirmationCodeView, ForgotPasswordView)

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

app_name = 'auth'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('change_image/<int:pk>/', UpdateUserImageView.as_view(), name='auth_image'),
    path('delete_profile/<int:pk>/', DeleteProfileView.as_view(), name='auth_delete_profile'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='auth_forgot_password'),
    path('confirm/', ValidateConfirmationCodeView.as_view(), name='auth_confirm'),
    path('reset_password/<int:pk>', ResetPasswordView.as_view(), name='auth_reset_password')
]
