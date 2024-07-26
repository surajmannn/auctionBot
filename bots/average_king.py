""" My Bot implementation based on my Student ID """

import random

class Bot(object):
    def __init__(self):
        self.name = "averageKing"
        # Add your own variables here, if you want to.

    def get_bid(
        self,
        current_round,
        bots,
        winner_pays,
        artists_and_values,
        round_limit,
        starting_budget,
        painting_order,
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

        # Determines if the bot shouldn't bet on the current painting
        def avoid_bid(current_painting, my_collection):
            bid = False
            two_or_more = 0

            artists = ['Da Vinci', 'Picasso', 'Rembrandt', 'Van Gogh']

            # Check if we don't own any of this artists paintings - bid
            if my_collection[current_painting] < 1:
                return False
            # Check if i should avoid bidding as i already have 3 of paintings from this artist - don't bid
            if my_collection[current_painting] == 3:
                return True
            # check if i already have 2 paintings from this artist - bid
            if my_collection[current_painting] == 2:
                return False
            
            # Remove current artist from list to avoid clash
            artists.remove(current_painting)
            
            # Check if there are already 2 artists in my collection with more than 1 painting - don't bid
            if my_collection[current_painting] < 2:
                for artist in artists:
                    if my_collection[artist] >= 2:
                        two_or_more += 1
                if two_or_more >= 2:
                    return True
            
            # check utility and remaining painting list?
            # No avoid bidding conditions met - bid
            return bid


        my_collection = my_bot_details['paintings']

        my_bid = 1001/8

        if(avoid_bid(current_painting, my_collection)):
            bid = 0
        else:
            bid = int(my_bid)

        return bid
