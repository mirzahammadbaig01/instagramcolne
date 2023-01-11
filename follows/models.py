from django.db import models
from accounts.models import User
class Follow(models.Model):
  follower=models.ForeignKey(User,on_delete=models.CASCADE, related_name='follower')
  following=models.ManyToManyField(User, related_name='following')
  status=models.BooleanField('Pending',default=True)
  def get_following(self):
        return "\n".join([u.email for u in self.following.all()])
# Create your models here.
