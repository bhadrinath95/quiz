from django.contrib import admin
from .models import Category, Quiz, Question, Answer,Result

# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display=('name','url_id')
admin.site.register(Category,AdminCategory)
class AdminQuiz(admin.ModelAdmin):
    list_display=('name','numberOfQuestions','category')
admin.site.register(Quiz,AdminQuiz)
class AdminQuestion(admin.ModelAdmin):
    list_display=('title','right_ans')
admin.site.register(Question,AdminQuestion)
class AdminAnswer(admin.ModelAdmin):
    list_display=('question','answer','status','user','add_time')
admin.site.register(Answer,AdminAnswer)
class AdminResult(admin.ModelAdmin):
    list_display=('category','user','start_time','end_time','total_questions','total_right_answers','total_score')
admin.site.register(Result,AdminResult )