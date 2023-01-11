from django.contrib import admin
from follows.models import Follow
class FollowAdmin(admin.ModelAdmin):
  list_display=('follower','get_following','status')
admin.site.register(Follow,FollowAdmin)
# Register your models here.
