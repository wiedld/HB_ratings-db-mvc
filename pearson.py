
# # PSEUDO CODE OF HOW THIS WORKS!!!
# num_critics = len(common_critics)
# num = product_sum - ((film1_sum * film2_sum)/num_critics)
# den = sqrt((film1_sum_square - pow(film1_sum, 2) / num_critics) * \
#     (film2_sum_square - pow(film2_sum, 2)/num_critics))
# pearson = num/den

#!/usr/bin/env python
from math import sqrt
import model

def pearson(pairs):
    # Takes in a list of pairwise ratings and produces a pearson similarity

    series_1 = [float(pair[0]) for pair in pairs]
    series_2 = [float(pair[1]) for pair in pairs]

    print "series 1:", series_1
    print "series 2:", series_2

    sum1 = sum(series_1)
    sum2 = sum(series_2)

    squares1 = sum([ n*n for n in series_1 ])
    squares2 = sum([ n*n for n in series_2 ])

    product_sum = sum([ n * m for n,m in pairs ])

    size = len(pairs)

    numerator = product_sum - ((sum1 * sum2)/size)
    denominator = sqrt((squares1 - (sum1*sum1) / size) * (squares2 - (sum2*sum2)/size))

    if denominator == 0:
        return 0
    
    return numerator/denominator



def create_pairs_for_pearson():
    m = model.session.query(model.Movie).filter_by(movie_title="Toy Story").one()
    u = model.session.query(model.User).get(3)
    user_ratings = u.user_ratings

    #retrieve all other ratings for this object.
    other_ratings = model.session.query(model.Rating).filter_by(movie_id=m.id).all()

    # determine each user who has also rated this same movie
    other_users = []
    for r in other_ratings:
        other_users.append(r.user)

    # iterate through each "other" in other-users, and creat list of aired reviews with our current user.
    for o in other_users:
        print "other user:", o
        paired_ratings = []
        for u_rating in user_ratings: #iterate each rating for our current user
            # print "this user's ratings:", o.user_ratings
            for o_rating in o.user_ratings:    #iterate each rating for o user
                if u_rating.movie_id == o_rating.movie_id:
                    paired_ratings.append( (u_rating.rating,o_rating.rating) )
        print "this is the data we are feeding in:", paired_ratings
        p_coefficient = pearson(paired_ratings)
        print "Pearson:", p_coefficient, "Other user:", o

create_pairs_for_pearson()
