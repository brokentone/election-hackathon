from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=25)

class Candidate(models.Model):
    full_name = models.CharField(max_length=50) 
    name = models.CharField(max_length=50)
    wp_url = models.CharField(max_length=100)

class Statement(models.Model):
    wp_id = models.IntegerField()
    wp_url = models.CharField(max_length=100)
    question = models.CharField(max_length=200)
    date = models.DateTimeField('date spoken')
    topic = models.ForeignKey(Topic)
    candidate = models.ForeignKey(Candidate)
