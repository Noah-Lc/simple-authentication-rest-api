from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers


class UserProfileViewSet(generics.CreateAPIView):
    """Handle creating profiles."""

    serializer_class = serializers.UserProfileSerializer

class LoginViewSet(ObtainAuthToken):
    """Check email and password and returns an auth token."""

    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManagerUserProfileViewSet(generics.RetrieveUpdateAPIView):
    """Handle Retrieve and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    queryset = get_user_model().objects.all()
