from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = patterns('blog.views',
	url(r"^$", "main"),

	url(r'^(?P<pk>\d+)$', DetailView.as_view(
		model = Post,
		template_name="post.html")),

	url(r'^archives/$', ListView.as_view(
		queryset=Post.objects.all().order_by("-created_at"),
		template_name="postlist.html")),

	url(r'^latestnews/$', ListView.as_view(
		queryset=Post.objects.all().order_by("-created_at")[:5],
		template_name="postlist.html")),

)