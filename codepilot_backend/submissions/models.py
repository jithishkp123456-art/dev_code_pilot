from django.db import models

# Create your models here.
from account.models import User
from assessments.models import Assessment

class Submission(models.Model):

    student=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    assessment=models.ForeignKey(
            Assessment,
            on_delete=models.CASCADE,
            related_name="assessments"
        )

    STATUS_CHOICES=[
        ("in-progress","in-progress"),
        ("submitted","submitted")
    ]

    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default="in-progress")

    start_time=models.DateTimeField(auto_now_add=True)

    submission_time=models.DateTimeField(null=True,blank=True)

    total_marks=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)

    EVALUATION_CHOICES=[
        ("pending","pending"),
        ("evaluated","evaluated"),
        ("released","released")
    ]

    evaluation_state=models.CharField(max_length=50,choices=EVALUATION_CHOICES,default="pending")

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.student.username} - {self.assessment.title}"
