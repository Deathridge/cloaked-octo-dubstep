from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = patterns('',
						url(r'^$', ListView.as_view(
								queryset=Post.objects.all().order_by("-created_at")[:10],
								template_name="blog.html")),

						url(r'^(?P<pk>\d+)$', DetailView.as_view(
								model = Post,
								template_name="post.html")),

)