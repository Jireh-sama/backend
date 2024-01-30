from django.contrib import admin
from .models import Student, Subject, Department, Instructor, Course, PayFees, Payments, SubjectEnrollment

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Instructor)
admin.site.register(PayFees)
admin.site.register(Payments)
admin.site.register(SubjectEnrollment)









