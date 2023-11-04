from rest_framework import serializers
from .models import Donat, Donator, Student, Universitet


class UniversitetSerializers(serializers.ModelSerializer):
     class Meta:
          model = Universitet
          fields = '__all__'


class DonatSerializers(serializers.ModelSerializer):
     class Meta:
          model = Donat
          fields = '__all__'


class DonatorSerializers(serializers.ModelSerializer):
     class Meta:
          model = Donator
          fields = '__all__'


class DonatorCreateSerializers(serializers.ModelSerializer):
     class Meta:
          model = Donator
          fields = [
               'full_name',
               'phone_number',
               'company',
               'balance',
               'legil',
               'company'
          ]


class StudentSerializers(serializers.ModelSerializer):
     class Meta:
          model = Student
          fields = [
               'full_name',
               'phone_number',
               'universitet',
               'statuc',
               'contract',
               'balance'
          ]

class StudentCreateSerializers(serializers.ModelSerializer):
     class Meta:
          model = Student
          fields = [
               'full_name',
               'phone_number',
               'universitet',
               'statuc',
               'contract'
          ]