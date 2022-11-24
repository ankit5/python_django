from django.db import models



# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length = 250)
  description = models.TextField(null=True)
  image = models.ImageField(upload_to='uploads/products/',null=True)

  def __str__(self):
     return self.title

# Create your models here.