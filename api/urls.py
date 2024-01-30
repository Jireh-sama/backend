from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views
from .views import StudentViewSet, PaymentsViewSet



router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'payments', PaymentsViewSet)


urlpatterns = [
  path('', include(router.urls)),
  path('get_grades/<str:pk>/', views.enrolled_subjects, name='grades'),
  path('get_payments/<str:pk>/', views.get_payments, name='get_payments'),
  path('register/', views.create_student, name='register'),
  path('login/', views.login_student, name='login'),


  
  # path('update_payments/<str:pk>/', views.update_payments, name='update_payments'),
  # path('get_all_payments/', views.get_all_payments, name='get_all_payments'),
  # path('create_student/', views.create_student, name='create_student'),
  # path('create_user/', CustomUserCreateView.as_view(), name='create_user'),
  # path('get_course/', views.get_course, name='get_course'),
  # path('get_students/', views.get_students, name='students'),
  # path('get_students/<str:pk>/', views.get_student, name='student'),
]