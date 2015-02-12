from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

PER_PAGE = 20


@app.route("/")
def index():
    # TODO when link to user list, user page 1.
    # TODO when link to movie list, movie page 1.
    pass


@app.route('/user_list/<int:page>')  
# next page link goes to this route
def show_user_list(page):
    """Takes info from Users table, and pulls for the Ratings table the total # of ratings done by that user (e.g. # of movies rated), displays users with pagination"""

    offset = (page-1) * PER_PAGE
    user_list = model.session.query(model.User).limit(PER_PAGE).offset(offset)
    # So each time this function is called, it gets the expected page number from jinja, which increments or decrements the page number based on which link the clicks
    return render_template("user_list.html", users=user_list, page_num=page)


@app.route("/user_details/<int:id>")
def show_user_details():
    """Takes info from Users, Ratings (# of ratings), and Movies (title of movies rated) tables.  And displays for each user.  Private details (emails) not included."""
    pass



@app.route("/movie_list/<int:page>")
def show_movie_list(page):
    """Pulls info from the Movies table and paginates it. May includes the average rating underneath each title it it's not too too hard to implement."""
    offset = (page-1) * PER_PAGE
    movie_list = model.session.query(model.Movie).limit(PER_PAGE).offset(offset)
    # So each time this function is called, it gets the expected page number from jinja, which increments or decrements the page number based on which link the clicks
    return render_template("movie_list.html", movies=movie_list, page_num=page)



@app.route("/movie_details/<int:id>")
def show_movie_details():
    """shows details for all reviews of this movies, as well as the movie details itself."""
    pass

@app.route("/login")
def user_login():
    """Shows user sign in form, can also link to the new user form. """
    pass

@app.route("/new_user")
def create_new_user():
    """Form where the user would create a new login, only redirects back to the login page to allow the user to login. Should flash a message that account create suceeded or failed on the sign in page. """
    pass

# @app.route("/edit_profile")
# def user_profile_edit():
#     """User is directed here from the view profile page. Not in MVP, implement if time."""
#     pass

@app.route("/review_movie")
def edit_create_review(movie_id):
    """Form for a user to submit a new review for a movie or to update a review they previously submitted """
    # if user in ratings has movie_id(rating):
    #     list_passed_to_webpage = current review (to be update)
    # else:  (movie not yet reviewed)
    #     list_passed_to_webpage = user info, movie info
    # return render_template("assads.html")
    pass


if __name__ == "__main__":
    app.run(debug=True)


