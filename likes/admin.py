from django.contrib import admin
from likes.models import Like
class LikeAdmin(admin.ModelAdmin):
  list_display=('id','user','post')
admin.site.register(Like,LikeAdmin)
# Register your models here.
