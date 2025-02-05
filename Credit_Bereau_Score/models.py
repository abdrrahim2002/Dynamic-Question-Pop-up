from django.db import models

# Create your models here.

class Question(models.Model):
  title = models.CharField(max_length=300)
  discreption = models.CharField(max_length=400)
  option_1 = models.CharField(max_length=200)
  option_2 = models.CharField(max_length=200)
  option_3 = models.CharField(max_length=200)
  option_4 = models.CharField(max_length=200)

  def __str__(self):
    return self.title
  
class UserProfile(models.Model):
  username = models.CharField(max_length=100)
  credit_score = models.IntegerField(default=0)

  def __str__(self):
    return self.username
  

class UserResponse(models.Model):
  user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  selected_option = models.CharField(max_length=200)
  score = models.IntegerField(default=0)

  def __str__(self):
    return f'{self.user_profile} response to {self.question.title}'