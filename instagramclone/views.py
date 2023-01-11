from django.shortcuts import render
from accounts.models import User
from posts.models import Post
from follows.models import Follow
from stories.models import Story
def homePage(request):
   user=User.objects.first()
   user_list=User.objects.all()
   bb=[]
   bb.append(user.email)
   follow=Follow.objects.filter(follower= user)
   for f in follow:
      if f.status==True:
         bb.append(f.get_following())
   posts= Post.objects.filter(user__email__in = bb)
   print (posts.first().post_image.url)
   stories= Story.objects.filter(user__email__in =bb)
   data={
     "user": user,
     "posts": posts,
     "stories": stories,
     "suggestions":user_list,
   }
   return render(request, "home.html",data)

