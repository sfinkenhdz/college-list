from django.shortcuts import render
from rest_framework import viewsets
from colleges.models import College, Attribute, Student
from django.contrib.auth.models import User
from colleges.serializers import CollegeSerializer, UserSerializer, AttributeSerializer, StudentSerializer
from rest_framework import permissions
from colleges.permissions import IsOwnerOrReadOnly

# Create your views here.

class CollegeViewSet(viewsets.ModelViewSet):
    """
    You can 'list', 'create', 'retrieve', 'update', and 'destroy' a college instance.
    """
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
      serializer.save(owner=self.request.user)

class AttributeViewSet(viewsets.ModelViewSet):
  queryset = Attribute.objects.all()
  serializer_class = AttributeSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
