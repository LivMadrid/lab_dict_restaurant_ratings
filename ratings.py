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

