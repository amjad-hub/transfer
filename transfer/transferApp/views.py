from django.shortcuts import render
from django.views.generic import CreateView
from .models import user_account,transfer
#from .forms import transferForm
from .serializers import transferSerializer,user_accountSerializer
from rest_framework import generics

#Create your views here.


class transferView(generics.ListCreateAPIView):
    queryset = transfer.objects.all()
    serializer_class = transferSerializer

class user_accountView(generics.ListCreateAPIView):
    queryset = user_account.objects.all()
    serializer_class = user_accountSerializer

