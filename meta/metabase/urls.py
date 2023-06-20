
from django.urls import path
from .views import embed_question

urlpatterns = [
    path('', embed_question, name='dashboard'),

]




# from django.urls import re_path as path

# from .views import *


# urlpatterns = [
#     url(r'', home, name='homepage')
# ]