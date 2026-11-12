from django.urls import path
from question.views import QuestionListCreateView,QuestionRetrieveUpdateDeleteView


urlpatterns = [
    path('question/',QuestionListCreateView.as_view()),
    path('question/<int:pk>/',QuestionRetrieveUpdateDeleteView.as_view()),
    
]