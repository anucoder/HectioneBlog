from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField()
    content = models.TextField()
    updated_on = models.DateField()
    created_on = models.DateField()
    author = models.CharField(max_length=100)
    #status =

    def __str__(self):
        return(self.title)
