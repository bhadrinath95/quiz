from django.shortcuts import render,HttpResponse,redirect
from .models import Quiz,Question,Answer,Category,Result
from .forms import GenerateQuizForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.contrib import messages
import requests
import random 
from django.db.models import Count
from django.utils import timezone
import datetime

# Create your views here.
class Register(View):
    def get(self,request):
        form=UserCreationForm
        return render(request,'registration/register.html',{'form':form})
    
    def post(self,request):
        saveForm=UserCreationForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'User is created successfully')
        else:
            messages.error(request,'User creation is failed')
        return redirect('/accounts/register')
    
class Home(View):
    template_name='home.html'
    def get(self,request):
        quiz=Quiz.objects.all()
        users=User.objects.all().order_by('-id')
        return render(request,self.template_name,{'data':quiz,'users':users})
    
class AllQuestion(View):
    template_name='category.html'
    def get(self,request,cat_id):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        page=request.GET.get('page',1)
        category=Quiz.objects.get(id=cat_id)
        result = Result.objects.get_or_create(user=request.user, category = category)
        data=Question.objects.filter(category=category)
        paginator=Paginator(data,1)
        data=paginator.get_page(page)
        submittedAnswer=False   
        for quest in data:
            try:
                answer=Answer.objects.filter(question=quest,user=request.user).get()
                submittedAnswer=answer.answer
            except Answer.DoesNotExist:
                submittedAnswer=False
        return render(request,self.template_name,{'data':data,'category':category,'submittedAnswer':submittedAnswer})
    def post(self,request,cat_id):
        if 'page' in request.GET:
            page=request.GET['page']
        else:
            page=1
        question=Question.objects.get(id=request.POST['q_id'])
        check=Answer.objects.filter(question=question,user=request.user).count()
        category=Quiz.objects.get(id=cat_id)
        if check == 0:
            if question.right_ans == request.POST['quest']:
                status=True
            else:
                status=False
            Answer.objects.create(
                user=request.user,
                category=category,
                question=question,
                answer=request.POST['quest'],
                status=status
            )
            if status:
                messages.success(request,'Correct Answer')
            else:
                messages.error(request, 'Wrong Answer')
            return redirect('/category/'+str(cat_id)+'?page='+str(page))
        else:
            messages.warning(request,'Already Answer Submitted!!')
            return redirect('/category/'+str(cat_id)+'?page='+str(page))
    
class CreateQuiz(View):
    template_name= 'generate_quiz'
    def get(self,request):
#         if request.user.is_superuser or (request.user.is_authenticated and request.user.is_admin):
        if request.user.is_authenticated:
            form= GenerateQuizForm
            return render(request, 'generateQuizForm.html', {'form':form})
        else:
            return HttpResponse('Unauthorized', status=401)
    
    def post(self, request):
        if request.user.is_authenticated:
            saveForm = GenerateQuizForm(request.POST)
            if saveForm.is_valid():
                name = saveForm.cleaned_data['name']
                numberOfQuestions = saveForm.cleaned_data['numberOfQuestions']
                cat = saveForm.cleaned_data['category']
                inst = saveForm.save()
                category = Quiz.objects.get(pk= inst.pk)
                if cat.name == "Any Category":
                    url = "https://opentdb.com/api.php?amount="+str(numberOfQuestions)+"&type=multiple"
                else:
                    url = f"https://opentdb.com/api.php?amount={numberOfQuestions}&category={cat.url_id}&type=multiple"
                print(url)
                response = requests.get(url)
                result = response.json()
                for i in result['results']: 
                    title = i['question']
                    answers = i['incorrect_answers']
                    answers.append(i['correct_answer'])
                    random.shuffle(answers) 
                    right_ans = i['correct_answer']
                    obj = Question(category=category, title= title, answer_1= answers[0], answer_2= answers[1], answer_3= answers[2], answer_4= answers[3], right_ans= right_ans) 
                    obj.save()
                
                    
            questions = Question.objects.filter(category=category)    
            form= GenerateQuizForm
            return render(request, 'generateQuizForm.html', {'form':form, 'questions': questions})
        else:
            return HttpResponse('Unauthorized', status=401)
    
    
class QuizResult(View):
    def get(self,request,cat_id):
        category=Quiz.objects.get(id=cat_id)
        question_count = Answer.objects.filter(user=request.user,category=category).count()
        right_ans = Answer.objects.filter(user=request.user,category=category,status=True).count()
        result_inst = Result.objects.get(user=request.user,category=category)
        if result_inst.end_time is None:
            result_inst.end_time= timezone.now()
            result_inst.total_questions = question_count
            result_inst.total_right_answers  = right_ans
            score=right_ans*100/question_count
            result_inst.total_score = score
            result_inst.save()
            
        duration = result_inst.end_time - result_inst.start_time
        return render(request, 'quizresult.html', {'result_inst':result_inst, 'duration':  int(duration.total_seconds() / 60) % 60 })

class ShowResult(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        results = Result.objects.filter(user=request.user)
        return render(request,'result.html',{
            'results':results
        })