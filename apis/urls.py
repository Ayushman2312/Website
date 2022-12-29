from django.urls import path
from .views import *

urlpatterns = [
    path('listview', StudentListAPIView.as_view(), name="listview"),
    path('<int:pk>/delete/', StudentDeleteAPIView.as_view(), name="deleteview")
]
