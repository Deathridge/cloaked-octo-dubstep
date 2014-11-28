from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post, Comment


urlpatterns = patterns('blog.views',
	url(r"^$", "main"),

	url(r"^(\d+)/$", "post"),	

	url(r"^add_comment/(\d+)/$", "add_comment"),

	url(r"^delete_comment/(\d+)/$", "delete_comment"),

	url(r"^delete_comment/(\d+)/(\d+)/$", "delete_comment"),

	url(r'^archives/$', ListView.as_view(
		queryset=Post.objects.all().order_by("-created_at"),
		template_name="postlist.html")),

	url(r'^latestnews/$', ListView.as_view(
		queryset=Post.objects.all().order_by("-created_at")[:5],
		template_name="postlist.html")),

)