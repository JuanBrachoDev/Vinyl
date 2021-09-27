from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response


# A view that returns the url request for spotify to authorize
class AuthURL(APIView):
    def get(self, request, fornat=None):
        scopes = 'user-read-email'

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)
