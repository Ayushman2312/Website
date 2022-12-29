# from django.shortcuts import render
from rest_framework.response import Response
from .serializers import StudentSerializer
from Students.models import StudentData
from rest_framework import generics, mixins
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

class StudentListAPIView(ListAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentSerializer

class StudentDeleteAPIView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
       return self.destroy(request, *args, **kwargs)




