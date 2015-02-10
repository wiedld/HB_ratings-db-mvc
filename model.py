from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None
Base = declarative_base()

### Class declarations go here
class User(Base):

    __tablename__ = "Users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

    def __repr__(self):
        """Show info about the Python User object"""

        return "<User id: %d, email: %s, password: %s, age: %d, zipcode: %s>" % (self.id, self.email, self.password, self.age, self.zipcode)



class Movie(Base):

    __tablename__ = "Movies"
    
    id = Column(Integer, primary_key = True)
    movie_title = Column(String(64), nullable=True)
    release_date = Column(String(10), nullable=True)
    IMDb_url = Column(String(64), nullable=True)

    def __repr__(self):
        """Show info about the Python Movie object"""

        return "<Movie id: %d, movie_title: %s, release_date: %s, IMDb_url: %s>" % (self.id, self.movie_title, self.release_date, self.IMDb_url)



class Rating(Base):

    __tablename__ = "Ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    movie_id = Column(Integer, ForeignKey("Movies.id"), nullable=False)
    rating = Column(Integer, nullable=False)

    def __repr__(self):
        """Show info about the Python Rating object"""

        return "<user_id: %d, movie_id: %d, rating(0-5): %d>" % (self.user_id, self.movie_id, self.rating)


### End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()


def main():
    """In case we need this for something"""
    pass


if __name__ == "__main__":
    main()
