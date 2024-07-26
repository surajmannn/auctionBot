""" My Bot implementation based on my Student ID """

import random

class Bot(object):
    def __init__(self):
        self.name = "utility_bot"
        # Add your own variables here, if you want to.

    def get_bid(
        self,
        current_round,
        bots,
        winner_pays,
        artists_and_values,
        round_limit,
        starting_budget,
        painting_order,         # useless
        target_collection,
        my_bot_details,
        current_painting,
        winner_ids,
        amounts_paid,
    ):
        """Strategy for collection type games.

        Parameters:
        current_round(int): 			The current round of the auction game
        bots(dict): 					A dictionary holding the details of all of the bots in the auction
                                                                        For each bot, you are given these details:
                                                                        bot_name(str):		The bot's name
                                                                        bot_unique_id(str):	A unique id for this bot
                                                                        paintings(dict):	A dict of the paintings won so far by this bot
                                                                        budget(int):		How much budget this bot has left
                                                                        score(int):			Current value of paintings (for value game)
        winner_pays(int):				Rank of bid that winner plays. 1 is 1st price auction. 2 is 2nd price auction.
        artists_and_values(dict):		A dictionary of the artist names and the painting value to the score (for value games)
        round_limit(int):				Total number of rounds in the game - will always be 200
        starting_budget(int):			How much budget each bot started with - will always be 1001
        painting_order(list str):		A list of the full painting order
        target_collection(list int):	A list of the type of collection required to win, for collection games - will always be [3,2,1]
                                                                        [5] means that you need 5 of any one type of painting
                                                                        [4,2] means you need 4 of one type of painting and 2 of another
                                                                        [3,2,1] means you need 3 of one type of painting, 2 of another, and 1 of another
        my_bot_details(dict):			Your bot details. Same as in the bots dict, but just your bot.
                                                                        Includes your current paintings, current score and current budget
        current_painting(str):			The artist of the current painting that is being bid on
        winner_ids(list str):			A list of the ids of the winners of each round so far
        amounts_paid(list int):			List of amounts paid for paintings in the rounds played so far

        Returns:
        int:Your bid. Return your bid for this round.
        """

        # WRITE YOUR STRATEGY HERE FOR COLLECTION TYPE GAMES - FIRST TO COMPLETE A FULL COLLECTION

        # Design

        # This function works out the amount of paintings for each artist in the current auction,
        # ...and returns the values in a alphabetically ordered list
        def analyse_frequency(painting_list):
            # alphabetically store frequency of artists paintings in the auction
            # Index Logic: [0] = Da Vinci, [1] = Picasso, [2] = Rembrandt, [3] = Van Gogh
            painting_frequency = [0,0,0,0]

            for name in painting_list:
                if name == 'Da Vinci':
                    painting_frequency[0] = painting_frequency[0] + 1
                if name == 'Picasso':
                    painting_frequency[1] = painting_frequency[1] + 1
                if name == 'Rembrandt':
                    painting_frequency[2] = painting_frequency[2] + 1
                if name == 'Van Gogh':
                    painting_frequency[3] = painting_frequency[3] + 1
            
            return painting_frequency


        # Assigns utility to painitings in the auction based on the painting list
        def assign_utility(painting_list, painting_frequency):

            # initialise utility array based on amount of paintings in auction
            utility = [0]*len(painting_list)
            painting_frequency = painting_frequency
            budget = 1001

            # create utility assignment based on painting order for the auction and frequency
            for index, artist in enumerate(painting_list):
                if artist == 'Da Vinci':
                    utility[index] = int((budget/8) * (1 - ((painting_frequency[0] * (8/200)) / 8)))

                if artist == 'Picasso':
                    utility[index] = int((budget/8) * (1 - ((painting_frequency[1] * (8/200)) / 8)))

                if artist == 'Rembrandt':
                    utility[index] = int((budget/8) * (1 - ((painting_frequency[2] * (8/200)) / 8)))

                if artist == 'Van Gogh':
                    utility[index] = int((budget/8) * (1 - ((painting_frequency[3] * (8/200)) / 8)))
            
            return utility


        # Determine average bid from winning bid based on artist in question    
        def average_bid(winning_bids, artist):

            # check winning bid values for current artist

            # potentially adjust bid?

            return 0


        # Adjust remaining paintings utilities based on my bots current collection
        def collection_adjustment(my_collection):

            # Return adjusted utility based on remaining paintings needed for success and paintings list?
            return 0


        # Analyses which competitors are near the winning condition
        def competitors(competitor_collection):

            # Take list which has competitors close to winning and their remaining budget

            # adjust utility again?
            return 0


        # Determines if the bot shouldn't bet on the current painting
        def avoid_bid(current_painting, my_collection):

            # Check if i should avoid bidding as the painting is not in my interest

            # check utility and remaining painting list?
            return 0


        # Master function
        def create_bid(current_painting, my_collection, my_remaining_budget, current_bid):

            # Determine amount of paintings per artist in auction
            painting_frequency = analyse_frequency(painting_order)

            # check utility
            utility = assign_utility(painting_order, painting_frequency) 

            # check my current collection

            # check whether should avoid painting

            # check competitors

            # update utility

            # average bid check for current painting
            # create bid based on utility, collection, competitors close to winning, and average bid for the current artist

            bid = 0

            return bid
        
        # my_bid = create_bid(current_painting, my_collection, remaining_budget, current_bid)
        # return my_bid
        
            
        #print("\n {} \n".format(my_bot_details['paintings']))
        
        current_budget = my_bot_details["budget"]
        remaining = 8 - sum(my_bot_details['paintings'].values())
        daVinci = my_bot_details['paintings']['Da Vinci']
        picasso = my_bot_details['paintings']['Picasso']
        rembrandt = my_bot_details['paintings']['Rembrandt']
        vanGogh = my_bot_details['paintings']['Van Gogh']

        frequency = analyse_frequency(painting_order)
        #print(frequency)
        #print(painting_order)
        utility = assign_utility(painting_order, frequency)
        #print(utility)

        return utility[current_round-1]
        
        #print(remaining, daVinci, picasso, rembrandt,vanGogh)

        #return random.randint(int((current_budget/8)*0.8), int(current_budget/8))
