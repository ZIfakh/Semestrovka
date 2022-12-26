from django.contrib import auth
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView

# Create your views here.


class LoginView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return Response(model_to_dict(user))
        else:
            print("Пользователя не существует")

        return Response(status=200)


class LogoutView(APIView):

    def post(self, request):
        email = request.user.username
        print(f'Logged out {email}')
        auth.logout(request)
        return Response(status=200)