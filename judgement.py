from flask import Flask, render_template, redirect, request, flash, session
import model
import pearson

app = Flask(__name__)
app.secret_key = 'imsosecretemwahahaha'


PER_PAGE = 20


@app.route("/")
def index():
    """User signs in on the home page, and signing in should redirect them to the rate movie page."""
    # TODO:  a real homepage.  (We just did a quick login here.)
    return render_template("login.html")



@app.route('/user_list/<int:page>')  
# next page link goes to this route
def show_user_list(page):
    """Takes info from Users table, and pulls for the Ratings table the total # of ratings done by that user (e.g. # of movies rated), displays users with pagination"""

    offset = (page-1) * PER_PAGE
    user_list = model.session.query(model.User).limit(PER_PAGE).offset(offset)
    # So each time this function is called, it gets the expected page number from jinja, which increments or decrements the page number based on which link the clicks
    return render_template("user_list.html", users=user_list, page_num=page)



@app.route("/user_details/<int:id>")
def show_user_details(id):
    """Takes info from Users, Ratings (# of ratings), and Movies (title of movies rated) tables.  And displays for each user.  Private details (emails) not included."""

        # see if the id fed into the function (the user info your are trying to see), matches who you are as a logged in user. 
    if session['logged_in'] == id:
        secure = True
    else:
        secure = False

    if id==0:       #brand new user
        return render_template("user_details.html", user=None, secure=secure, pg_id=id)
    else:
        user_details = model.session.query(model.User).get(id)
        return render_template("user_details.html", user = user_details, secure=secure,pg_id=id)



@app.route("/user_info/<int:id>")
def update_user(id):
    """Routed here after a user profile is created or edited. This function updates the database, flashes a message that account was created or updated, and redirects to another page (user_list/1 for now). """
    if id>0:
        # TODO:  db logic to overwrite.
        flash("Your profile has been updated.")
    elif id==0:
        # TODO:  db logic to insert into table
        flash("Your account has been created.")
    return redirect("/user_list/1") 



@app.route("/login")
def user_login():
    """Shows user sign in form, can also link to the new user form. """
    # Hardcode this so we're always signed in as a given user.
    # TODO:  compare login info provided to database.  Update session with correct user id.
    session['logged_in'] = 3
    return redirect("/recommendations")



@app.route("/movie_list/<int:page>")
def show_movie_list(page):
    """Pulls info from the Movies table and paginates it. May includes the average rating underneath each title it it's not too too hard to implement."""

    offset = (page-1) * PER_PAGE
    movie_list = model.session.query(model.Movie).limit(PER_PAGE).offset(offset).all()
    num_of_ratings=[]

    for movie_obj in movie_list:
        list_of_ratings = movie_obj.movie_ratings
        num_of_ratings.append(len(list_of_ratings))
    
    movie_info = zip(movie_list, num_of_ratings)
    # So each time this function is called, it gets the expected page number from jinja, which increments or decrements the page number based on which link the clicks
    return render_template("movie_list.html", movies=movie_info, page_num=page)



@app.route("/recommendations/")
def show_recommendations():
    """Pulls info from the Movies table and paginates it. May includes the average rating underneath each title it it's not too too hard to implement."""

   
    movie_list = model.session.query(model.Movie).all()
    # num_of_ratings=[]

    # for movie_obj in movie_list:
    #     list_of_ratings = movie_obj.movie_ratings
    #     num_of_ratings.append(len(list_of_ratings))
    
    # movie_info = zip(movie_list, num_of_ratings)
    # So each time this function is called, it gets the expected page number from jinja, which increments or decrements the page number based on which link the clicks
    return render_template("recommendations.html", movies=movie_info)



@app.route("/movie_details/<int:id>")
def show_movie_details():
    """shows details for all reviews of this movies, as well as the movie details itself."""
    # TO DO:  DETAILS PER movie.id!
    return render_template("movie_details.html")



@app.route("/review_movie/<int:id>")
def edit_create_review(id):
    """Form for a user to submit a new review for a movie or to update a review they previously submitted """
    #TODO:   none of this is completed yet.
    #movie = GET MOVIE DETAILS, feed into template.
    #TODO: update template file, with movie details.
    #TODO: submit off the template page for the review, back to a route which incorporates the new rating into the db.
    return render_template("review.html, movie=movie")



if __name__ == "__main__":
    app.run(debug=True)
