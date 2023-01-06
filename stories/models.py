from django.db import models
from accounts.models import User
class Story(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  story_images=models.FileField(upload_to="stories/",max_length=250,null=False)
  timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

# Create your models here.
