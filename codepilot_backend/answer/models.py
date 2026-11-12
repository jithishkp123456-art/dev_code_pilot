from django.db import models
from submissions.models import Submission
from question.models import Question
# Create your models here.
class Answer(models.Model):

    submission=models.ForeignKey(Submission,on_delete=models.CASCADE,related_name="answer")

    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="answer")

    answer_text= models.TextField()

    awarded_marks=models.FloatField(default=0)

    feedback=models.CharField(max_length=200)


    def __str__(self):
        return f"{self.submission}-{self.question}"
