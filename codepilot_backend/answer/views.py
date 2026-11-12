from django.shortcuts import render
from answer.models import  Answer
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView
from answer.models import Answer
from answer.serializers import AnswerSerializer
# Create your views here.
class AnswerCreateView(CreateAPIView):
    serializer_class=AnswerSerializer


