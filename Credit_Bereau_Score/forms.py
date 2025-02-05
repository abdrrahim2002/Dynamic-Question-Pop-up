from django import forms
from .models import Question

class question_1(forms.Form):
  username_1 = forms.CharField(
    max_length=100, 
    required=True, 
    widget=forms.TextInput(attrs={'title': 'Personal information'}),
    label='Username'
    )




#create a dynamic forms generator

#get all the question from the datadase

Question_all = Question.objects.all()

#dictionary to store dynamically generated form classes
dynamic_forms = {}

#loop through each question to create a form class for it

for count,question in enumerate(Question_all, start=2):

  #define the choices fo the radio buttons
  options = [
    ('option 1', question.option_1),
    ('option 2', question.option_2),
    ('option 3', question.option_3),
    ('option 4', question.option_4),
  ]

  #define a dictionaru of form fields
  form_fields = {
    f'question_{count}': forms.ChoiceField(
      choices=options,
      widget=forms.RadioSelect(attrs={'title': question.title}),
      label=question.discreption,
      required=True
    )
  }

  form_class_name = f'QuestionForm_{count}'
  form_class = type(form_class_name, (forms.Form,), form_fields)

  dynamic_forms[form_class_name] = form_class

  
  #now dynamic_forms contains each dynamically generated form class



  