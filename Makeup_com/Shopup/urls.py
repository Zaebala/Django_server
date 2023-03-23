from django.urls import path
from Shopup.views import *

urlpatterns = [
    path('', main),
    path('add/', additem),
    path('relog/', login),
    path('reg/', reg),
    path('acc/', acc)
]
