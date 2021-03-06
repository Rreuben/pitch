# Minute-Pitch

<p align = "center">
    <b>By Rreuben</b>  
</p>

### Description
Oneminutepitch is a web based application that allows you to pitch ideas, comment on the ideas, vote on the pitch they like, and give it a downvote or upvote. The pitches are further grouped in categories, allowing users to interact in any of them.

***
#### The app specifications 
This website will:

    Display pitches other people have posted.
    As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.
    Allow a user to sign in to leave a comment.
    Send a welcoming email once a user signs up.
    Allow a user to view the pitches they have created in their profile page.
    Allow a user to comment on the different pitches and leave feedback.
    Allow a user to submit a pitch in any category.
    Display different categories.

#### Technologies
* HTML
* Python
* Flask (in Python)
* Bootstrap (for styling)
* Postgresql (the database)

View the source code at [GitHub](https://github.com/Rreuben/pitch)

#### Installation/Setup
You need to have Python 3.6 installed to run this program.

`$ git clone <this-repository>`<br />

Create a virtual enironment and activate it.

`$ virtualenv -p python`<br />
`$ source virtual/bin/acivate` and `(virtual)$ deactivate` is to deactivate the environment.

In the virtual environment:

`(virtual)$ pip install -r requirements.txt`<br />

Running the app.

    Prepare the environment variables.
    
        (virtual)$exportDATABASE_URL='postgresqlpsycopg2://username:password@localhost/pitch'`<br/>
        `(virtual)$ export SECRET_KEY='Your secret key'

    Run Database Migrations.

        (virtual)$ python manage.py db init
        (virtual)$ python manage.py db migrate -m "Initial migration"
        (virtual)$ python manage.py db upgrade

    Run the app.

        (virtual)$ touch start.sh

        Put #!/usr/bin/env bash as the first line in start.sh
        Put python3.6 manage.py server as the second line in start.sh

        (virtual)$ chmod a+x start.sh
        (virtual)$ ./start.sh

#### Alternatively
* Open browser (Google Chrome Recommended)
* Visit the live [website](https://pitttch.herokuapp.com)

#### Further Development
Some features that are to come soon:

    Pitch voting system and like and dislike function.
    Pitch viewing on the user's profile.
    Commenting and feedback features.
    Categories.
    
#### Known Bugs
Apparently heroku cannot pick up cdn links, so if you open this project you might see no navbar. However, you can still sign in but there is no button for signing out. 

***

<p align = "center">
    <a href = "https://github.com/Rreuben/pitch/blob/master/LICENSE">LICENSE</a>
</p>
