# Forum Website With Django

Web Development 

- Built a website allowing UMass students to create and view survey and discussion posts from other UMass students
- Website allows secured login functionality for UMass students and students can vote on survey posts and view results in the form of a pie chart
- Wrote in Python, HTML5, CSS, and JavaScript programming languages to create and style different web pages, add functionality, and store data to database
- Used the Model-View-Template (MVT) architecture of Django to write methods in model, views, and forms python files and created several HTML5 template files to render the webpages


# Overview 
Our application is a forum for UMass students that allows users to create discussion posts and survey posts. Users can create discussion posts by entering a title and the content of the discussion. Users can create survey posts by entering a question and giving multiple choice options for others to choose from. The authors of survey posts can also select how they want the results to be displayed: a poll percentage, bar chart or pie chart. Users can also upload images and comment on posts. The aim is to provide more ways for UMass students to communicate, and to see how the community at large feels on certain topics. 

Our web app is particularly innovative in the way it can collect relevant data and present it in a clean and efficent way. Our web app is also much better at creating a sense of community when compared to other similar platforms like Reddit or Yahoo. The information shared on our platform will be made by Umass students for Umass students in a way that hasnt been done before.  


# Team Members
* Conor Carmichael
* Stephen Ulich
* Monmoy Mohsin
* Harsha Malireddy
* Arjun Singh
* Kyle Ewell

# Design Overview
For this submission Django user accounts were created, allowing login/logout functionality similar to the examples done in class. The users were created in the init.py file. Since we already had a UserAccount model created which was linked to other data types we had to link the new users to the existing user accounts with a one to one mapping which included changing the model of userAccount to accept a user as a one to one field. 

For user interaction, we used Django forms to implement fields that users can use to create and update discussion posts. In our template, we checked to see whether a user is authenticated, is a superuser, or is neither of those. This allowed us to handle each case, by directing authorized users to the form, throwing a message to super users to use the admin site, and throwing a message to login for users.

In terms of functionality, we decided that users will not be allowed to modify survey posts because it could lead to dishonest data and would defeat the purpose of allowing surveys. We also decided to not allow users to delete posts because they could delete useful information in their posts or in the responses. Only admins will be allowed to delete posts if the content is deemed inappropriate.


# User Interface 

This is the main landing page when a user first logs in to the site, which will show some basic statistics about the website, and allow the user to access the content he/she desires.
![HomePage IMG](/homepage.png "HomePage")

This is what the user will see when they attempt to log in to the site.
![Login IMG](/login.png "Login")

This is what the user will see when they log out of the site.
![Logout IMG](/logout.png "Logout")

This is the main discussions page that displays all the latest discussion posts. This particular UI is meant to filter by 'most recent' and all user posts would end up here, functionlaity will be added in future to be able to keep posts private or to specific users.
![discussionPage IMG](/discussionPage.png "Discussions")

Similar to the discussion page above, mainly meant to just present the surveys created by all users on the site. Also allows users to vote live on page and see results. 
![surveyPage IMG](/surveyPage.png "Surveys")

Page that displays all personal contributions to the site.
![yourPosts IMG](/yourPosts.png "Your Posts")

The page that holds the form to submit one of the discussions to be promoted to the front page.
![discussionForm IMG](/discussionForm.png "Discussion Form")

The page shows an example of the results of a survey post being displayed in a pie chart.
![surveyResults IMG](/surveyResults.png "Survey Resutls")


# Data Model 
We have 6 models in our models.py file: UserAccount, DiscussionPost, CommentSection, SurveyPost, Choice, Document. The UserAccount model identifies different users which contains a username, a first name, and a last name. The DiscussionPost contains information regarding a post, including the title, the author (a UserAccount object), the content of the post, and a reference to a comment section. The comment is tied to the discussion post, many comments can link to one discussion post and each content contains a user, and text. The SurveyPost model contains a title, a UserAccount, a question, and the options that can be voted for. The options are found in the Choice model and are a different data model where many different instances of Choice can link to one survey post. Each instance of a Choice contains the actual option and the number of votes that the option has received. Our 6th model document describes the details of the documents uploaded by the user. It contains the author field, uploaded_at field that describes the time it was uploaded, description field that explains the uploaded image and the document field.
![FinalDataModel IMG](/FinalDataModel.png "Final Data Model")


# URL Routes/Mappings 

|  Urls    |     Description                                                                                             |
|----------|:-----------------------------------------------------------------------------------------------------------:|
| “”                                              | This is the homepage of the website.                                 |                                        
|"surveyposts/"                                   | This page displays the list of survey posts.                         |                            
|"createsurvey/"                                  | This goes to a form to create a survey.                              |                               |"discussionposts/"                               |  This page displays the list of discussion posts.                    |                            
|"surveyresults/".             | This page displays the list of survey posts with the option of picking an answer choice.|                                                                                                       
|"discussioncreation/"                            | This goes to a form to create a discussion.                          |       
|r'^surveyresults/(?P<pk>[0-9A-Fa-f-]+)'          | This displays the survey results of each individual survey post.     |       
|r'^discussionposts/(?P<pk>[0-9A-Fa-f-]+)'        | This displays each discussion post where it displays each discussion |
|                                                 |  post in detail where it gives you the option to edit the post.      |                
|"user/"                                          | This goes to each users homepage.                                    |                                       
|"docUpload/"                                     | This displays the page to upload images.                             |
|"imageposts/"                                    | This displays the list of images uploaded.                           |
|r'^discussionposts/(?P<pk>[0-9A-Fa-f-]+)/update/'| This displays each discussion post form to edit the discussion post  |
|                                                 |  that was selected. Users can only edit their posts.                 |
|"discussionposts/"                               | This page displays the list of discussion posts.                     |

# Authentication/Authorization 
To check if users are already authenticated we write the condition {% if user.is_authenticated %}. If not, on certain views they will either be nudged to login, or they will need to login to continue. For example, the home page can be viewed if not logged in, but there will be some additional login buttons and prompts, if they aren’t and go to submit a discussion post, they will be shown a message indicating they must login to continue. The line {% if user.username == object.disc_author.user_name  %} helps ensure that only the user can only edit the post they create. We have a form set up through django to allow users to log in, which can be accessed via the navbar, and when authenticated they can post, view their profile.

# Team Choice 
For our team choice component we decided to add functionality that would allow users to upload images and view images posted by others. For this team choice we added the Document model in models.py. This model consisted of a image field, a description, a time uploaded, and an author field. To allow images to be added we created a docUpload.html page which interacts with forms.py to update the Document data model. This included additions to forms.py, views.py, and urls.py. We created a list view for the images that shows the images, the descriptions and the authors. This is shown in imageposts.html which also required additions to urls.py. Finally we added to the base.html to make these upload pages and viewing pages for the images easily accessible. 

# Conclusion 

As a team we came from varying levels of experience but were able to come together and form a cohesive group with the ability to accomplish anything. Throughout the submissions we learned how to work together as a team to get all the various tasks done but also we began to become proficient in HTML, CSS and Django. As time went on it was almost effortless for us to delegate tasks to each other and get everything from the tricky UI to the troublesome user authentication done.

As a team we couldn't think of any one particular thing that stood out to us as especially troubling other than a few things with User Authentication and generating user accounts. There was also a minor issue we ran into which was trying to link specific survey options to their respective survey post. We were able to resolve the issue, by figuring out how to add the parameter “related name = “choices”” in the survey_post foreign key element of the “Choice” model in the models.py file among other things. At times we left some of the work off a bit too long which left us scrambling so in the future we certainly plan on being more proactive with the project and its due dates and to not expect things to magically get done. 

We would of liked to know more about CSS techniques and design strategies for making things look more appealing. Of Course there's more demand for functionality and authentication but knowing how to create blocks of content and manipulating dimensions with inline style are important things to know too and could be covered in a class or two. Otherwise most things seemed useful to know as we went along with each submission. 

Other then a few issues with getting everybody hooked up on github, incidental or damaging github commits and the web servers we didn't really encounter any crazy technical errors. One error experienced, was a difference in OSX and Ubuntu, Conor was working with Ubuntu, others in OSX, and OSX didn’t seem react to capitalization in file paths for templates, but on Ubuntu these templates weren’t being located properly. After analyzing a bunch of the file paths, this was solved though, in urls.py some of the templates just had to be retyped, and all was solved. Everything more or less developed smoothly with everyone's efforts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
 
