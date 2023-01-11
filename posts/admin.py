from django.contrib import admin
from posts.models import Post
class PostAdmin(admin.ModelAdmin):
  list_display=('post_desc','post_image','user_id')
admin.site.register(Post,PostAdmin)
# Register your models here.
