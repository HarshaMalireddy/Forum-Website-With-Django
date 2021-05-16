from django import forms
from UMassApp.models import DiscussionPost, CommentSection, Document


class CreateDForm(forms.ModelForm):
	title = forms.CharField(max_length=25)
	content = forms.CharField(max_length=400)

	class Meta:
		model = DiscussionPost
		fields = ('title', 'content',)

class CreateCommentForm(forms.ModelForm):
	text = forms.CharField(max_length=400)

	class Meta:
		model = CommentSection
		fields = ('text',)

class DocumentForm(forms.ModelForm):
	description = forms.CharField(max_length=50)
	document = forms.ImageField()
	class Meta:
		model = Document
		fields = ('description', 'document',)