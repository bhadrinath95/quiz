# Online Quiz Application

• Online quiz application aids for the schools which wants to conduct online quiz for its students. Students should be able to start the quiz, get the questions, select their answers and view the results. 
• This Online quiz application uses [Open Trivia Database](https://opentdb.com/)for fetching the questions and answers.

## Instructions

• The school (i.e., Only Super user) can able create multiple quizzes with variable number of questions. 
• The questions are Multiple Choice Questions (MCQs). 
• User can start a quiz by clicking on the quiz name displayed in home screen.
• The results will be instant. After the user selects answer for a question, whether it is correct or incorrect will be shown immediately.
• Once a question is submitted, user will be allowed to see the next question. 
• At the end, the user can see the time it took to finish the quiz, how many correct answers the user got. 

## Hosting

• This Online quiz application is hosted in [Python Anywhere](https://www.pythonanywhere.com/).
• The URL of the application is **[Online Quiz Application](http://quizfortestpress.pythonanywhere.com/)**

## Installation

•	pip install django==3.1.5
•	pip install requests==2.25.1

## Software Versions Used

•	Python- 3.8.5
•	Django- 2.25.1
•	JQuery- 3.5.1
•	Bootstrap- 5.0.0
•	Requests- 2.25.1

## Getting Started

First clone the repository from Github

    $ git clone https://github.com/bhadrinath95/quiz
    $ cd quiz
    
Create a virtual environment

    $ mkvirtualenv --python=/usr/bin/python3.8 myenv
    
Install project dependencies:

    $ pip install django==3.1.5
    $ pip install requests==2.25.1
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    
You can create super user:

    $ python manage.py createsuperuser
    

You can perform unit testing:

    $ python manage.py test
