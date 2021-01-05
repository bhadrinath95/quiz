from django.urls import path
from .views import Home,Register,CreateQuiz,AllQuestion,ShowResult,QuizResult
urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('accounts/register',Register.as_view()),
    path('category/<int:cat_id>',AllQuestion.as_view(),name='category'),
    path('createQuiz',CreateQuiz.as_view(),name='createQuiz'),
    path('result/<int:cat_id>',QuizResult.as_view()),
    path('result',ShowResult.as_view()),
    
]