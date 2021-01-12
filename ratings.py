"""Restaurant rating lister."""


#     #Reads the ratings in from the file

#     #Stores them in a dictionary

#     #And finally, spits out the ratings in alphabetical order by restaurant

# Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.

# Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sor

# put your code here
def restaurant_ratings(filename):
    #open file
    rating_file = open(filename)
    # define empty dictionary 
    dict_restaurant_ratings = {}

    # go through file line by line 
    for line in rating_file:
        # parce into a list separating on colon 
        line_list = line.rstrip().split(":")
        # put ratings into dictionary 
        dict_restaurant_ratings[line_list[0]] = line_list[1]
        # set sorted keys to new list variable 
        sorted_restaurant_names = sorted(dict_restaurant_ratings)
        # loop through list variable 
        for name in sorted_restaurant_names:
            # print to the console restaurant name and rating
            print(f"{name} is rated at {dict_restaurant_ratings[name]}.")
    
    # get user input for restaurant name and score
    restaurant_name = input(f"Please enter a restaurant name:  ")
    restaurant_rating = input(f"Please enter a restaurant number: ")
    # store in dict_restaurant_ratings
    dict_restaurant_ratings[restaurant_name] = restaurant_rating
    # Sort again 
    sorted_restaurant_names = sorted(dict_restaurant_ratings)
    for name in sorted_restaurant_names:
        # Print them again
        print(f"{name} is rated at {dict_restaurant_ratings[name]}.")


# Modify your script so that after it reads the scores file from disk, it prompts the user for a new restaurant and rating.

# The program should:

#     Prompt the user for a restaurant name

#     Prompt the user for a restaurant score

#     Store the new restaurant/rating in the dictionary

#     Print all of the ratings in alphabetical order (including the new one, of course)



