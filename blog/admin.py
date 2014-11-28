from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_field = ["title"]
    
admin.site.register(Post, PostAdmin)
