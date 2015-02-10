import model
import csv

def load_users(session):
    
    user_file = open("./seed_data/u.user")

    for line in user_file:
        line_list = line.split("|")
        user_object = model.User()

        # This pulls attributes from the line of raw data & assigns to object
        user_object.id = int(line_list[0])
        user_object.age = int(line_list[1])
        user_object.zipcode = line_list[4]
        session.add(user_object)

    session.commit()


def load_movies(session):

    movies_file = open("./seed_data/u.item")

    for line in movies_file:
        line_list = line.split("|")
        movie_object = model.Movie()

        # this pulls attributes from the line of raw data & assigned to object
        movie_object.id = int(line_list[0])
        # This cleans up the title and strips release date from the title string
        title = line_list[1]
        title = title.decode("latin-1")
        movie_object.movie_title = title[:-7]

        movie_object.release_date = line_list[2]
        movie_object.IMDb_url = line_list[4]
        session.add(movie_object)

    session.commit()



def load_ratings(session):
    
    ratings_file = open("./seed_data/u.data")

    for line in ratings_file:
        rating_list = line.split()
        a_rating = model.Rating()

        a_rating.user_id = int(rating_list[0])
        a_rating.movie_id = int(rating_list[1])
        a_rating.rating = int(rating_list[2])

        session.add(a_rating)

    session.commit() 



def main(session):
    # You'll call each of the load_* functions with the session as an argument
    # load_users(session)
    # load_movies(session)
    load_ratings(session)




if __name__ == "__main__":
    s= model.connect()
    main(s)
