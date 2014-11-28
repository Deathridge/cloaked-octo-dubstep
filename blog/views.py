from django.shortcuts import render_to_response,render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from blog.models import *
from blog.forms import *
from django.core.context_processors import csrf

# Create your views here.

def main(request):
	"""Show all current posts in reverse chronological order"""
	posts = Post.objects.all().order_by("-created_at")
	paginator = Paginator(posts, 2)

	try: 
		page = int(request.GET.get("page", '1'))
	except ValueError: page = 1

	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)

	return render_to_response("blog.html", dict(posts=posts, user=request.user))

def post(request, pk):
	"""Allows commenting on individual posts"""
	post = Post.objects.get(pk=int(pk))
	comments = Comment.objects.filter(post=post)
	d = dict(post=post,comments = comments,form=CommentForm(), user=request.user)
	d.update(csrf(request))
	return render_to_response("post.html", d)