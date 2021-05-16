from django.contrib import admin

from UMassApp.models import UserAccount, DiscussionPost, CommentSection, SurveyPost, Choice, Document
@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):

    list_display = ("first_name","last_name","user_name")
    fields = ["first_name", "last_name", "user_name"]

class DiscussionPostInline(admin.TabularInline):
    model = DiscussionPost

@admin.register(DiscussionPost)
class DiscussionPostAdmin (admin.ModelAdmin):

    list_display = ("id", "title", "disc_author")
    fields = ["title", "disc_author", "content"]

class CommentSectionInline(admin.TabularInline):
    model = CommentSection

@admin.register(CommentSection)
class CommentSectionAdmin (admin.ModelAdmin):
 
    list_display = ("post", "text", "author")
    fields = ["post", "text", "author"]

class DiscussionPostInline(admin.TabularInline):
    model = DiscussionPost

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class SurveyPostAdmin (admin.ModelAdmin):

    list_display = ("id", "title", "survey_author", "question")
    fields = ["title", "survey_author", "question"]
    inlines = [ChoiceInline]


admin.site.register(SurveyPost, SurveyPostAdmin)

@admin.register(Choice)
class Choice (admin.ModelAdmin):

    list_display = ("survey_post", "option", "votes")
    fields = ["survey_post", "option","votes"]

class DocumentInline(admin.TabularInline):
    model = Document

@admin.register(Document)
class DocumentPostAdmin (admin.ModelAdmin):

    list_display = ("id", "description", "author", "uploaded_at")
    fields = ["description", "author", "uploaded_at"]



