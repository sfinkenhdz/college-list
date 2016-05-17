from rest_framework import serializers
from colleges.models import College, Attribute, Student
from django.contrib.auth.models import User


class CollegeSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  # attributes = serializers.SlugRelatedField(
  #   many=True,
  #   read_only=True,
  #   slug_field='name'
  #   )
  class Meta:
      model = College
      fields = ('name', 'size', 'url', 'owner', 'attributes')

class AttributeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Attribute
    fields = ('name', 'category', 'url')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    colleges = serializers.PrimaryKeyRelatedField(many=True, queryset=College.objects.all())
    class Meta:
      model = User
      fields = ('id', 'username', 'colleges', 'url')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Student
    fields = ('name', 'college_list', 'url')