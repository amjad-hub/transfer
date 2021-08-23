from django.contrib import admin
from django.urls import path
from .views import transferView,user_accountView

urlpatterns = [ 

    path('transfer/', transferView.as_view(),name='transfer'),
    path('accounts/', user_accountView.as_view(),name='accounts'),
]
