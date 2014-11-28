from django.db import models

# Create your models here.
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length = 140)   
    body = models.TextField()
    published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.CharField(max_length = 60) 
    body = models.TextField()
    post = models.ForeignKey(Post)
    

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))

