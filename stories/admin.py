from django.contrib import admin
from stories.models import Story
class storyAdmin(admin.ModelAdmin):
  list_display=('story_images','timestamp')
# Register your models here.
admin.site.register(Story,storyAdmin)
