"""
The serializer converts our model instances to a 
data type that the response object can understand
"""
from rest_framework import serializers
from base.models import Student, Course, PayFees, Subject, SubjectEnrollment, Payments
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# from django.contrib.auth.models import User


class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subject  
    fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'

class PayFeesSerializer(serializers.ModelSerializer):
  eligable_courses = CourseSerializer(many=True, read_only=True)
  class Meta:
    model = PayFees
    fields = '__all__'

class PaymentsSerializer(serializers.ModelSerializer):
   pay_fee = PayFeesSerializer()
   class Meta:
    model = Payments
    fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
  enrolled_subjects = SubjectSerializer(many=True, read_only=True)
  class Meta:
    model = Student
    fields = '__all__'
    
class SubjectEnrollmentSerializer(serializers.ModelSerializer):
   subject = SubjectSerializer()
   class Meta:
    model = SubjectEnrollment
    fields = '__all__'



