from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, Factory
from django.db.models import Count
# Create your views here.


class UserView(View): 

    def get(self,request):
        if request.user.is_authenticated:
            order_obj = Order.objects.filter(user=request.user)
            return render(request, "order.html", {"user": order_obj})
        else:
            return Response(status=500)


class Count_beer(View):

    def get(self, request):
        pubs = Order.objects.annotate(num_books=Count('title'))
        return render(request, 'count.html', {"count": pubs[1].num_books})


def main(requset):
    return render(requset, 'index.html')


def index(request):
    return render(request, 'count.html')

