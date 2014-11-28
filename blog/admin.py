from django.contrib import admin
from blog.models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_field = ["title"]
    
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
	display_fields = ['post', 'author', 'created_at']

admin.site.register(Comment, CommentAdmin)
