from django.db import models
from django.conf import settings
from accounts.models import User
class Post(models.Model):

   user = models.ForeignKey(User,on_delete=models.CASCADE)
   post_image=models.FileField(upload_to="post/",max_length=250,null=False)
   post_desc=models.TextField('Post Description', max_length=500,null=True, default=None)
   def __str__(self):
      return self.post_desc
# Create your models here.
