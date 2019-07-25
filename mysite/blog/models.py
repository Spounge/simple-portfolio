from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publication date')
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
