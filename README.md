# __Journee__

Journee is a platform that gives you the freedom to journal the important parts of your life, either just for you or for others. It’s a great way to capture a single page for that day along with a photo and selfie if you wish. You then have a chronological history of all the things you want to look back on in years to come. It’s a great way to stay connected with your journey through life and share it with others!

## Planning

### Core Features ###

The core purpose of the site is to provide an online journal to users. I wanted to strip back the noise that most social sites come with and focus users on distilling their content down. By deafult users pages are not made public so it becomes a private jounral.

1 Page and photo per day


__Users__

* Frictionless Sign Up & Sign In
* View/search public journals without an account (Entices Sign Up)
* Showcase journal entries on the landing page
* Select journal page theme
* Create one page per day


__Site Admins__

* Change Journal Pages to private


### Agile Planning ###

I used the agile method to plan out Journee and you can review all my Epics and User Stories in the Project linked to this repo [__Here__](https://github.com/users/Will-Griffiths-Ireland/projects/2/views/2)

I took the role > action > benfit approach to writing my user stories

## Database Design

## User interface Design

All my intial wireframe concepts can be found here in a PDF.

The basic layout of the site aims to be simple and intuitive


## Features

### User Account Creation



### View Count

* Each journal entry has functionality to track how many views it has had.
* This allows a user to know how many others viewed their public journal page.
* The count is also used in picking content for the showcase page.
* The logic delibrately counts every single view to allow for a simulated production expereince during testing and review.
* With a launched site this functionality would be modified to use something like Django-Hitcount so that only unique views per IP would be counted

## Testing

## Technoligies & Tools

* Bootstrap 5.3
* Jquery 3.7.0
* Django

## Deployment

* clone repo
setup db
setup cloud storage
deploy to Heroku

## Future Enhancements

* Full encrption of all user journal and profile information
* Ability to search users based on their description words
* Ability to follow other users and have a dedicated page view of their pages

## Credits & Acknowlegements

* Boot strap docs
* Django docs