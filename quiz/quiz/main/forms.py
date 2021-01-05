from django import forms
from .models import Quiz

class GenerateQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
                "name",
                "numberOfQuestions",
                "category",
            ]