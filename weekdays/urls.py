from django.urls import path
from .views import *

urlpatterns = [
    path('weekdays/',hafta,name='hafta'),
    path('weekdays/uz/',hafta_uz,name='hafta_uz'),
    path('weekdays/ru/',hafta_ru,name='hafta_ru'),
    path('weekdays/eng',hafta_eng,name='hafta_eng'),

]