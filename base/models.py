from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# =============================================
# Members: Jireh Tumbagahan and Arvie Tokong
# =============================================
YEARLVL_CHOICES = [
    (1, "1st Year"),
    (2, "2nd Year"),
    (3, "3rd Year"),
    (4, "4th Year"),
]

class Student(models.Model):
    SEX_CHOICES = [("male", "Male"), ("female", "Female")]
    SEM_CHOICES = [(1, "1st Semester"), (2, "2nd Semester")]
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=8, choices=SEX_CHOICES, default="male")
    age = models.PositiveIntegerField(null=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=155, null=True)
    student_number = models.CharField(
        max_length=11, unique=True, blank=True, null=True, verbose_name="Student Number"
    )
    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True)

    # payments = models.ManyToManyField("PayFees", blank=True)
    enrolled_subjects = models.ManyToManyField("Subject", blank=True)

    year_level = models.PositiveIntegerField(
        choices=YEARLVL_CHOICES, default=1, verbose_name="Year Level"
    )
    semester = models.PositiveIntegerField(choices=SEM_CHOICES, default=1)

    def __str__(self):
        return self.last_name
    
    # Method to assign the generated student number
    # if the value is not set on save
    def save(self, *args, **kwargs):
        if not self.student_number:
            self.student_number = self.generate_student_number()
        super().save(*args, **kwargs)

    # Method to automatically generate a student number 
    # format is YYYYMM + last five digit of the current millisecond
    def generate_student_number(self):
        current_year = datetime.now().year
        current_month = datetime.now().month
        current_datetime = datetime.now()
        current_milliseconds = int(current_datetime.timestamp() * 1000)
        last_five_digits = str(current_milliseconds % 100000).zfill(3)
        return str(current_year) + str(current_month).zfill(2) + last_five_digits


class Subject(models.Model):
    REMARK_CHOICES = [("passed", "Passed"), ("failed", "Failed"), ("inc", "INC")]
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    instructor = models.ForeignKey("Instructor", on_delete=models.CASCADE, null=True)
    eligable_courses = models.ManyToManyField("Course")
    eligible_years = models.IntegerField(
        choices=YEARLVL_CHOICES,
        default=1,
    )

    def __str__(self):
        course_names = ", ".join(course.name for course in self.eligable_courses.all())
        subject_title = f"{self.code} - {course_names} - {str(self.eligible_years)}"
        return subject_title


class SubjectEnrollment(models.Model):
    REMARK_CHOICES = [("passed", "Passed"), ("failed", "Failed"), ("inc", "INC")]
    STATUS_CHOICES = [
        ("active", "Active"),
        ("dropped", "Dropped"),
        ("completed", "Completed"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="active")
    grade = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(1.00), MaxValueValidator(5.00)],
        help_text="Enter the student's grade on a scale from 1.00 to 5.00.",
        null=True,
        blank=True,
    )
    remark = models.CharField(
        max_length=20,
        choices=REMARK_CHOICES,
        null=True,
        blank=True,
    )
    feedback = models.CharField(max_length=50, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.subject_id:
            raise ValueError("Subject must be specified before saving.")
        
        # Check if the subject is enrolled for the student
        if self.subject not in self.student.enrolled_subjects.all():
            raise ValueError("Cannot enroll in a subject that the student is not associated with.")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.student.last_name + '-' + self.subject.code
    
class Course(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class PayFees(models.Model):
    description = models.CharField(max_length=50, null=True)
    eligable_courses = models.ManyToManyField("Course")
    amount = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return self.description
    
class Payments(models.Model):
    STATUS_CHOICES = [("paid", "Paid"), ("unpaid", "Not Paid")]
    student = models.ForeignKey(Student ,on_delete=models.CASCADE, null=True)
    date_assigned = models.DateTimeField(auto_now_add=True, null=True)
    pay_fee = models.ForeignKey(PayFees, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='unpaid')

    def __str__(self):
        return self.student.first_name + '-' + self.pay_fee.description


    
