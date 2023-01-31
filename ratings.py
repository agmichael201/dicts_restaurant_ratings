"""Restaurant rating lister."""

def reading_rating():
    
    file_name = open("scores.txt")
    ratings_dictionary = {}
    
    for line in file_name:
        line = line.rstrip()
        name_restaurant, rating = line.split(":")
        ratings_dictionary[name_restaurant] = int(rating)
        
    return ratings_dictionary


def adding_rating(ratings_dictionary):
    restaurant_name = input("Please provide us a restaurant name: ")
    restaurant_score = int(input("Please provide us a score: "))
    
    ratings_dictionary[restaurant_name] = restaurant_score


def print_scores(ratings_dictionary):
    for restaurant, rating in sorted(ratings_dictionary.items()):
        print(f'{restaurant} is rated {rating}')
    

# print(ratings_dictionary)

ratings_dictionary = reading_rating()

adding_rating(ratings_dictionary) 
print_scores(ratings_dictionary)