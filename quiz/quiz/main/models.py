from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    url_id = models.IntegerField()
    
    def __str__(self):
        return self.name    
    
class Quiz(models.Model):
    name = models.CharField(max_length=100)
    numberOfQuestions = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name  
    
class Question(models.Model):
    category=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    answer_1=models.CharField(max_length=500)
    answer_2=models.CharField(max_length=500)
    answer_3=models.CharField(max_length=500)
    answer_4=models.CharField(max_length=500)
    right_ans=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Answer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Quiz,on_delete=models.CASCADE, default=1)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.CharField(max_length=500,null=True)
    status=models.BooleanField(default=False)
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question.title
    
class Result(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Quiz,on_delete=models.CASCADE, default=1)
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    total_questions = models.IntegerField(null=True,blank=True)
    total_right_answers= models.IntegerField(null=True,blank=True)
    total_score = models.FloatField(null=True,blank=True)
    
    def __str__(self):
        return self.category.name