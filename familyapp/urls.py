from django.urls import path

from familyapp.views import *

urlpatterns = [
path('', family, name='family')

]