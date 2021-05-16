import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UserAccount(models.Model):
    """Model representing a user."""

    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     help_text="Unique ID for this user across whole platform",
    # )
    account = models.OneToOneField(
        User,
        related_name='UserAccount',
        null=True,
        on_delete=models.CASCADE,
        # primary_key=True,
    )
    # A character field for the first name.
    first_name = models.CharField(max_length=20)

    # A character field for the last name.
    last_name = models.CharField(max_length=20)

    # A charecter field for the username
    user_name = models.CharField(max_length=20)
 

    class Meta:
        ordering = ["user_name"]

    def get_absolute_url(self):
        """Returns the url to access a particular user"""
        return reverse("user-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.user_name}"

class DiscussionPost(models.Model):
    """Model representing a discussion post."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this post",
    )

    title = models.CharField(max_length=100)

    disc_author = models.ForeignKey("UserAccount", on_delete=models.SET_NULL, null=True)

    content=models.CharField(max_length=4000)

    comment_section= models.ForeignKey("CommentSection", on_delete=models.SET_NULL, null=True)

    class Meta:
       ordering = ["title"]

    def get_absolute_url(self):
        """Returns the url to access a particular discussion post"""
        return reverse("discussion-post-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.title}"


class CommentSection(models.Model):
    """Model representing a comment."""
    post = models.ForeignKey('DiscussionPost', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('UserAccount',on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=400)

class SurveyPost(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this post",
    )

    title = models.CharField(max_length=25)
    survey_author = models.ForeignKey("UserAccount", on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=200)
    # options =  models.ListTextField(
    #     base_field=IntegerField(),
    #     size=100,  # Maximum 
    # )
    options = models.ForeignKey("Choice", on_delete=models.SET_NULL, null=True)


    class Meta:
       ordering = ["title"]

    def get_absolute_url(self):
        """Returns the url to access a particular discussion post"""
        return reverse("survey-post-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.title}"

    # def getOptions(self):
        

class Choice(models.Model):

    survey_post = models.ForeignKey("SurveyPost",related_name="choices",on_delete=models.SET_NULL, null=True)
    option = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to = 'UMassApp/uploadedImages')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('UserAccount',on_delete=models.SET_NULL, null=True)

