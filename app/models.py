from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name
class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return str(self.topic_name)
class accessRecords(models.Model):
    name = models.ForeignKey(webpage,on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return str(self.name)
    
