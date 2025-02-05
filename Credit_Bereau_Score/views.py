from django.shortcuts import render
from .models import UserProfile, UserResponse, Question

from .forms import question_1, dynamic_forms
from formtools.wizard.views import SessionWizardView


# Create your views here.
#get all the question from the question model

all_question = Question.objects.all()


#create a helper dictionary to store the titles of the question

question_titles = {}

for count,question in enumerate(all_question, start=2):
  question_titles[f'question_{count}'] = question.title


#storing variables
option_selected = []

total_score = 0

#helper functions

def get_score_by_select(selcet):
  if (selcet == 'option 1'):
    return 10
  elif (selcet == 'option 2'):
    return 7
  elif (selcet == 'option 3'):
    return 4
  elif (selcet == 'option 4'):
    return 0


def calculate_result(options):
  total = 0
  for option in options:
    if option == 'option 1':
      total += 10
    elif option == 'option 2':
      total += 7
    elif option == 'option 3':
      total += 4
    elif option == 'option 4':
      total += 0
  return total




class form_score (SessionWizardView):
  form_list = [question_1] + list(dynamic_forms.values())

  template_name = 'Credit_Bereau_Score/index.html'

  def done(self, form_list, **kwargs):
    #create a dictionary to collect data
    datas = {}

    #reset the value helper to the default state
    total_score = 0
    option_selected = []

    for form in form_list:
      datas.update(form.cleaned_data)

    #start storing the datas:
    for data in datas :
      if (data == 'username_1'):
        ##save the user
        UserProfile.objects.create(
          username = datas.get(data)
      )
      else :
        UserResponse.objects.create (
          user_profile = UserProfile.objects.filter(username=datas.get('username_1')).latest('id'), # to get the last id of the use if there is a username withe the same name
          question = Question.objects.get(title=question_titles[f'{data}']),
          selected_option = datas.get(data),
          score = get_score_by_select(datas.get(data))
        )

        option_selected.append(datas.get(data))

    #save the user score
    total_score = calculate_result(option_selected)
    user_profile = UserProfile.objects.filter(username=datas.get('username_1')).latest('id')
    user_profile.credit_score = total_score
    user_profile.save()


    #the response
    return render(self.request, 'Credit_Bereau_Score/result.html', {
      'username': datas.get('username_1'),
      'score': total_score,
      'number_of_questions': (len(datas.items()) - 1) *10
    })
    
