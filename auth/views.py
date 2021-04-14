from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage

from api.models import Profile
from .serializers import (
    RegisterSerializer, ChangePasswordSerializer, UpdateProfileSerializer)

import random


class RegisterView(generics.CreateAPIView):
    """  """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
    """  """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateProfileSerializer


class UpdateUserImageView(APIView):
    parser_classes = (MultiPartParser, )
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk, format=None):
        user = request.user
        if user.pk != pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={
                'detail': {
                    "authorize": "you dont have permission for this user !"
                    }
                })
        if 'image' in request.data:
            profile = get_object_or_404(Profile, pk=pk)
            profile.image = request.data['image']
            profile.user = user
            profile.save()
            return Response(
                status=status.HTTP_200_OK, data={"detail": 'modified'})

        else:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'detail': {'not-valid': 'the image field data is missing'}})


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk, format=None):
        user = request.user
        if user.pk != pk:
            return Response(
                data={"detail": "unauthorized"},
                status=status.HTTP_401_UNAUTHORIZED)

        if 'password' not in request.data:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'detail': 'password-required'})

        if not user.check_password(request.data['password']):
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data={'detail': "password-incorrect"})

        user.is_active = False
        user.save()
        return Response(status=status.HTTP_200_OK, data={"detail": "deleted"})


class ForgotPasswordView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        if not 'email' or 'username' in request.data:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'detail': {'email_or_username': 'required'}})

        user = None
        if 'email' in request.data:
            user = get_object_or_404(User, email=request.data['email'])
        if 'user' in request.data:
            user = get_object_or_404(User, username=request.data['username'])
        mail_subject = 'Reset Your Password'
        server_code = random.randint(10000, 999999)
        message = 'Hi {0},\nthis is your email confirmation code:\n{1}'.format(user.first_name, server_code)

        to_email = user.email
        EmailMessage(mail_subject, message, to=[to_email]).send()
        request.session['code'] = server_code
        request.session['user'] = user.username
        return Response(status=status.HTTP_200_OK, data={'detail': "sent"})


class ValidateConfirmationCodeView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        if 'code' not in request.session and 'user' not in request.session:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'detail': 'session-not-found'})

        if 'code' not in request.data:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'detail': {"code": "required"}})

        if not int(request.data['code']) == int(request.session['code']):
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data={'detail': 'wrong-code'})
        username = request.session['user']
        return Response(
            status=status.HTTP_200_OK,
            data={'pk': get_object_or_404(User, username=username).pk})


class ResetPasswordView(APIView):
    """ """
    permission_classes = (AllowAny,)

    def put(self, request, pk, format=None):
        user = get_object_or_404(User, username=request.session['user'])
        if user.pk != pk:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={"detail": "unauthorized"})

        if not 'password' and 'again' in request.data:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'detail': {"password": "required", 'again': 'required'}})

        if request.data['password'] != request.data['again']:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'detail': 'not-matched'})

        user.set_password(request.data['password'])
        user.save()
        return Response(status=status.HTTP_200_OK, data={'detail': 'done'})
