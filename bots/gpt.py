""" My Bot implementation based on my Student ID """

import random

class Bot(object):
    def __init__(self):
        self.name = "chatgpt"
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

        """for bot in bots:
            print("\n {}: {}. Number of paintings so far: {} \n".format(bot['bot_name'], bot['paintings'], sum(bot['paintings'].values())))"""


        # WRITE YOUR STRATEGY HERE FOR COLLECTION TYPE GAMES - FIRST TO COMPLETE A FULL COLLECTION
            

        def determine_bid_amount(current_budget, current_total):
            """
            Determine the bid amount based on the current budget and remaining budget.
            """
            # Example bidding strategy: bid a random percentage of remaining budget
            max_bid = 1 - (current_total/10)
            bid_percentage = random.uniform(0.1, max_bid)  # Adjust range as needed
            bid_amount = bid_percentage*current_budget
            return bid_amount

        def avoid_overbidding(current_collection, target_collection):
            """
            Check if bidding should be avoided to prevent overbidding.
            """
            for i, target_count in enumerate(target_collection):
                if current_collection[i] >= target_count:
                    return True
            return False

        def bot_strategy(target_collection, my_bot_details):
            """
            Bot strategy to win the auction based on Nash Equilibrium.
            """
            my_bot_budget = my_bot_details['budget']
            current_collection = list(my_bot_details['paintings'].values())
            current_collection_total = sum(my_bot_details['paintings'].values())

            # Determine if bidding should be avoided to prevent overbidding
            if avoid_overbidding(current_collection, target_collection):
                bid_amount = 0
            else:
                # Determine bid amount based on current and remaining budget
                bid_amount = determine_bid_amount(my_bot_budget, current_collection_total)

            return bid_amount

        # Example usage:

        bid_amount = bot_strategy(target_collection, my_bot_details)
        return bid_amount