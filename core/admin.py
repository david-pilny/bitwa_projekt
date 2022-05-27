from django.contrib import admin
from .models import Profile, Post, LikePost, FollowerCount, Room, Message

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowerCount)
admin.site.register(Room)
admin.site.register(Message)
