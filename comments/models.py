from django.db import models
from posts.models import Post
from django.utils import timezone
from accounts.models import User
class Comment(models.Model):
  comment_body=models.TextField('Body', max_length=500,null=False, default=None)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  post = models.ForeignKey(Post,on_delete=models.CASCADE)
  comment_created_at = models.DateTimeField('Created at',default=timezone.now)
  def __str__(self):
        return self.comment_body
# Create your models here.
