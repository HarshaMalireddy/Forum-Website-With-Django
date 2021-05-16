import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker

from UMassApp.models import UserAccount, DiscussionPost, CommentSection, SurveyPost, Choice

fake = Faker()



# Create users
#creates users
createdUsers = []
users=[]
print("Generated users:")
for a in range(10):
    a_fname = fake.first_name()
    a_lname = fake.last_name()
    username = a_fname.lower()[0] + a_lname.lower()
    email = f"{username}@326.edu"
    password = a_lname
    user = User.objects.create_user(username, email, password)
    user.first_name = a_fname
    user.last_name = a_lname
    user.save()
    createdUsers.append(user)
    print(f"  username: {username}, password: {password}")
    newUser = UserAccount(
        account=user, first_name=a_fname, last_name=a_lname, user_name=username
    )
    newUser.save()
    users.append(newUser)








# users = []
# for i in range(1, 10):
#     a_fname = fake.first_name()
#     a_lname = fake.last_name()
#     user = UserAccount(
#         first_name=a_fname, last_name=a_lname, user_name=a_fname
#     )
#     user.save()
#     users.append(user)


# Create discussions
discussionPosts = []
for i in range(1, 20):
    a_title = fake.text(50)
    a_author = users[fake.random_int(0, len(users)) - 1]
    a_content = fake.text(500)
    post = DiscussionPost(title=a_title, disc_author=a_author, content=a_content)
    post.save()
    #post.genre.add(genres[fake.random_int(0, len(genres)) - 1])
    #post.save()
    discussionPosts.append(post)

comments = []
for i in range(1, 40):
    a_post = discussionPosts[fake.random_int(0, len(discussionPosts)) - 1]
    a_author = users[fake.random_int(0, len(users)) - 1]
    a_text = fake.text(200)
    comment= CommentSection(post=a_post, author=a_author, text=a_text)
    comment.save()
    comments.append(comment)

# Create surveys
surveyPosts = []
for i in range(1, 20):
    a_title = fake.text(50)
    a_author = users[fake.random_int(0, len(users)) - 1]
    a_content = fake.text(200)
    post = SurveyPost(title=a_title, survey_author=a_author, question=a_content)
    post.save()
    #post.genre.add(genres[fake.random_int(0, len(genres)) - 1])
    #post.save()
    surveyPosts.append(post)

options = []
for i in range(1, 100):
    a_post = surveyPosts[fake.random_int(0, len(discussionPosts)) - 1]
    a_option = fake.text(10)
    a_votes = fake.random_int(0,40)
    choice= Choice(survey_post=a_post, option=a_option, votes=a_votes)
    choice.save()
    options.append(choice)



username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)











