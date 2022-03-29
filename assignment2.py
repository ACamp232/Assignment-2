
from imdb import Cinemagoer

 
ia = Cinemagoer()


def text_to_dict(text):
    """return a dictionary that records the frequencies of all the words in text"""
    review_dict = {}
    for word in text.split():
        # print(word)
        review_dict[word] = review_dict.get(word, 0) + 1
    return review_dict

def search_for_words(r):
    """Tells whether a key word is used in the review"""
    print ('sci-fi appears:', r.get('sci-fi'))
    print ('book appears:', r.get('book'))
    print ('dystopian appears:', r.get('dystopian'))
    print ('violence appears:', r.get('violence'))
    print ('futuristic appears:', r.get('futuristic'))
    print ('scary appears:', r.get('scary'))
    print ('villains appears:', r.get('villains'))
    



def interpret_key_words():
    """"creates a list with the most frequent key words from each movies reviews """
    kw_list_hg = ["book", "dystopian", "violence"]
    print ('Based on the reviews of The Hunger Games', kw_list_hg[0], ',',kw_list_hg[1], ', and' ,kw_list_hg[2], 'would be great words to describe the movie')
    kw_list_p = ["violence", "futuristic"]
    print ('Based on the reviews of The Purge', kw_list_p[0], ', and', kw_list_p[1], 'would be great words to decribe the movie')
        

def main():
    """Repeats the process of finding the reviews, words and printing results for each movie anf their review"""
    ia = Cinemagoer()

    # search the movie and find movie id 
    movie = ia.search_movie('The Hunger Games')[0]
    # print(movie.movieID)
    # Hunger Games movie id : 1392170

    print('The first review for the Hunger Games contains the following words...')
    movie_reviews_hg = ia.get_movie_reviews('1392170') # specifies which movie to use, this is Hunger Games 
    hunger_games_review_1 = movie_reviews_hg['data']['reviews'][0]['content'] # specifies which review to use, this is the first review 
    d = text_to_dict(hunger_games_review_1)
    f = search_for_words(d)
    print(f)
    
    #repeat for other reviews of the same movie(2 more)
    print('The second review for the Hunger Games contains the following words... ')
    hg_review_2 = movie_reviews_hg['data']['reviews'][1]['content']
    d = text_to_dict(hg_review_2)
    f = search_for_words(d)
    print(f)
    
    print ('The third review for the Hunger Games contains the following words...')
    hg_review_3 = movie_reviews_hg['data']['reviews'][2]['content']
    d = text_to_dict(hg_review_3)
    f = search_for_words(d)
    print(f)

    # The Purge movie id: 2184339
    print('The first review for The Purge contains the following words...')
    movie_reviews_p = ia.get_movie_reviews('2184339') 
    p_review_1 = movie_reviews_p['data']['reviews'][0]['content']
    g = text_to_dict(p_review_1)
    h = search_for_words(g)
    print(h)

    print('The second review for The Purge contains the following words...')
    p_review_2 = movie_reviews_p['data']['reviews'][1]['content']
    g = text_to_dict(p_review_2)
    h = search_for_words(g)
    print(h)

    print('The third review for The Purge contains the following words...')
    p_review_3 = movie_reviews_p['data']['reviews'][2]['content']
    g = text_to_dict(p_review_3)
    h = search_for_words(g)
    print(h)

    interpret_key_words()

   

if __name__ == "__main__":
    main()