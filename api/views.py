#Response Object - take in any python data that is passed into it and render it out as json data#
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, viewsets
from base.models import Student, Course, PayFees, SubjectEnrollment, Payments
from .serializers import *
# from django.contrib.auth.models import User


#api_view contains all the allowed request methods

# endpoint to get all students
@api_view(['GET'])
def get_students(request):
  students = Student.objects.all()
  serializer = StudentSerializer(students, many=True)
  return Response(serializer.data)

# end point to get a single student 
# by providing a primary key  
@api_view(['GET'])
def get_student(request, pk):
  try:
    student = Student.objects.get(id=pk)
  except Student.DoesNotExist:
    raise Http404('Student does not exist')
  serializer = StudentSerializer(student, many=False)
  return Response(serializer.data)


@api_view(['POST'])
def login_student(request):

  data = request.data
  try_email = data.get('email')
  try_password = data.get('password')

  student = Student.objects.get(email=try_email)
  print(student.password)
  if try_password == student.password:
    serializer = StudentSerializer(student)
    return Response(serializer.data)

  return Response('Not FOund')

  

#endpoint to create a student
@api_view(['POST'])
def create_student(request):
  serializer = StudentSerializer(data=request.data)

  if serializer.is_valid():
      data = request.data
      # Fetch subjects eligible for the provided course and year level
      course_id = data.get('course')
      year_lvl = data.get('year_level')
      
      default_subjects = Subject.objects.filter(eligable_courses=course_id, eligible_years=year_lvl)
      default_payments = PayFees.objects.filter(eligable_courses=course_id)

      # Create the student
      student = serializer.save()

      # Associate fetched subjects with the newly created student
      student.enrolled_subjects.add(*default_subjects)

      # Iterate throgh the subjects and create their own
      # Subject enrollment object associated with the created student and subject
      for subject in default_subjects:
       SubjectEnrollment.objects.create(student=student, subject=subject)

      for payment in default_payments:
        Payments.objects.create(student=student, pay_fee=payment)

      return Response(serializer.data, status=status.HTTP_201_CREATED)

  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def update_payments(request, pk):
  try:
    instance = Payments.objects.get(id=pk)
  except:
    return Response({"error": "Object not Found"}, status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = PaymentsSerializer(instance, many=False)
    return Response(serializer.data)
  
  if request.method == 'PUT':
    serializer = PaymentsSerializer(instance, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   


@api_view(['GET']) 
def enrolled_subjects(request, pk):
  try:
    enrolled_subjects = SubjectEnrollment.objects.filter(student_id=pk)
    serialized_data = SubjectEnrollmentSerializer(enrolled_subjects, many=True).data
    return Response(serialized_data, status=status.HTTP_200_OK)
  except SubjectEnrollment.DoesNotExist:
    return Response({"detail": "Student not found or has no enrolled subjects."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_payments(request, pk):
  try:
    payments = Payments.objects.filter(student_id=pk)
    serialized_data = PaymentsSerializer(payments, many=True).data
    return Response(serialized_data, status=status.HTTP_200_OK)
  except Payments.DoesNotExist:
    return Response({"detail": "Payments not found or has no assigned payments."}, status=status.HTTP_404_NOT_FOUND)
  


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class PaymentsViewSet(viewsets.ModelViewSet):
  queryset = Payments.objects.all()
  serializer_class = PaymentsSerializer
##############################################################
# @api_view(['GET'])
# def get_subject(request, pk):
#   try:
#     subject = Subject.objects.get(id=pk)
#   except Student.DoesNotExist:
#     raise Http404('Student does not exist')
#   serializer = StudentSerializer(student, many=False)
#   return Response(serializer.data)


@api_view(['GET'])
def get_course(request):
  courses = Course.objects.all()
  serializer = CourseSerializer(courses, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_fees(request):
  fees = PayFees.objects.all()
  serializer = PayFeesSerializer(fees, many=True)
  return Response(serializer.data)

@api_view(['POST'])
#Method to add data#
def add_data(request):
  serializer = StudentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

