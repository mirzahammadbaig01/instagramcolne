from django.db import models
from accounts.models import User
from posts.models import Post
class Like(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  post = models.ForeignKey(Post,on_delete=models.CASCADE)
def __str__(self):
    return self.id

# Create your models here.
