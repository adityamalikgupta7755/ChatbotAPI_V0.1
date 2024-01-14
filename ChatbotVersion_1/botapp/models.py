from django.db import models

# Create your models here.
class Questionlist(models.Model):
    question = models.TextField()
    def __str__(self):
        return self.question
    
class Chathistory(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
    


    