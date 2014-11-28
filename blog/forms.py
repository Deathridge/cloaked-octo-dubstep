from django.forms import ModelForm
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ["post"]

def add_comment(request, pk):
	"""add a new comment"""

	p = request.POST

	if p.has_key("body") and p["body"]:
		author = "Anonymous"
		if p["author"]: author = p["author"]

		comment = Comment(post = Post.objects.get(pk=pk))
		cf = CommentForm(p, instance=comment)
		cf.fields["author"].required = False

		comment = cf.save(commit = False)
		comment.author = author
		comment.save()
	return HttpResponseRedirect(reverse("blog.views.post", args=[pk]))

def delete_comment(request,post_pk, pk=None):
	"""form for comment deletion"""
	if request.user.is_staff:
		if not pk: pklst = request.POST.getlist("delete")
		else: pklst = [pk]

	for pk in pklst:
		Comment.objects.get(pk=pk).delete()
	return HttpResponseRedirect(reverse("blog.views.post", args=[post_pk]))