from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from main.forms import GenerateQuizForm
from main.models import Category

# Create your tests here.
class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john1', 'lennon@thebeatles.com', 'johnpassword')

    def testLogin(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)
        
class GenerateNewQuizFormTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Temp Cat", url_id=100)

    def test_verify_label(self):
        form = GenerateQuizForm()
        self.assertTrue(form.fields['name'].label == "Name" and form.fields['numberOfQuestions'].label == "NumberOfQuestions" and form.fields['category'].label == "Category")
    
    def test_verify_form(self):
        cat = Category.objects.get(name="Temp Cat")
        form = GenerateQuizForm(data={'name': "TestForm", "numberOfQuestions": 2, "category":cat})
        self.assertTrue(form.is_valid())    
        
    def test_verify_not_proper_form(self):
        cat = Category.objects.get(name="Temp Cat")
        form = GenerateQuizForm(data={'name': "TestForm", "category":cat})
        self.assertFalse(form.is_valid())    