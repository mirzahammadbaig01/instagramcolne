from django.contrib import admin
from comments.models import Comment
class CommentAdmin(admin.ModelAdmin):
  list_display=('comment_body','user','post','comment_created_at')
admin.site.register(Comment,CommentAdmin)
# Register your models here.
