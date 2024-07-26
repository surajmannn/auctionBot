""" My Bot implementation based on my Student ID """

import random

class Bot(object):
    def __init__(self):
        self.name = "u5591185"
        # Add your own variables here, if you want to.

        # initialise lists to store winning bid prices for each artist
        self.mean_price_davinci = []
        self.mean_price_picasso = []
        self.mean_price_rembrandt = []
        self.mean_price_vangogh = []

        # initialise average winning bid values
        self.average_winning_davinci = 1
        self.average_winning_picasso = 1
        self.average_winning_rembrandt = 1
        self.average_winning_vangogh = 1

        # alphabetically store frequency of artists paintings in the auction
        # Index Logic: [0] = Da Vinci, [1] = Picasso, [2] = Rembrandt, [3] = Van Gogh
        self.painting_frequency = [0,0,0,0]

        # intial array for holding each paintings utility based on the order of paintings
        self.utility = []


    # This function works out the amount of paintings for each artist in the current auction,
    # ...and returns the values in a alphabetically ordered list
    def analyse_frequency(self, painting_list):
        for name in painting_list:
            if name == 'Da Vinci':
                self.painting_frequency[0] = self.painting_frequency[0] + 1
            if name == 'Picasso':
                self.painting_frequency[1] = self.painting_frequency[1] + 1
            if name == 'Rembrandt':
                self.painting_frequency[2] = self.painting_frequency[2] + 1
            if name == 'Van Gogh':
                self.painting_frequency[3] = self.painting_frequency[3] + 1
    

    # Assigns utility to painitings in the auction based on the painting list
    def assign_utility(self, painting_list):
        # initialise utility array based on amount of paintings in auction
        self.utility = [0]*len(painting_list)
        painting_frequency = self.painting_frequency
        budget = 1001

        # create utility assignment based on painting order for the auction and frequency
        # Utility is calculated as percentage based on frequency and current budget consider the number of paintings for winning condition
        for index, artist in enumerate(painting_list):
            if artist == 'Da Vinci':
                self.utility[index] = round((budget/8) * (50 / painting_frequency[0]), 3)

            if artist == 'Picasso':
                self.utility[index] = round((budget/8) * (50 / painting_frequency[1]), 3)

            if artist == 'Rembrandt':
                self.utility[index] = round((budget/8) * (50 / painting_frequency[2]), 3)

            if artist == 'Van Gogh':
                self.utility[index] = round((budget/8) * (50 / painting_frequency[3]), 3)


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

        # Initialise class variables at the start of the auction to be used during the auction
        if current_round == 0:
            # check utility
            self.analyse_frequency(painting_order)
            self.assign_utility(painting_order)

        # Gives the frequency as a ratio between 0-1 of the current artist in the auction so far and the average bid of the artist           
        def return_frequency_average(artist):
            this_round = max(1, current_round-1)
            # Calculates the frequency of artist in wins compared to overall round
            #... also returns the current average winning bid of the current artist
            if artist == 'Da Vinci':
                current_auction_frequency = len(self.mean_price_davinci) / this_round
                average = self.average_winning_davinci
            if artist == 'Picasso':
                current_auction_frequency = len(self.mean_price_picasso) / this_round
                average = self.average_winning_picasso
            if artist == 'Rembrandt':
                current_auction_frequency = len(self.mean_price_rembrandt) / this_round
                average = self.average_winning_rembrandt
            if artist == 'Van Gogh':
                current_auction_frequency = len(self.mean_price_vangogh) / this_round
                average = self.average_winning_vangogh

            return current_auction_frequency, average
        

        # Updates the average winning bid for each artist during the auction 
        def update_average_bid():
            if self.mean_price_davinci:
                self.average_winning_davinci = sum(self.mean_price_davinci) / len(self.mean_price_davinci)
            if self.mean_price_picasso:
                self.average_winning_picasso = sum(self.mean_price_picasso) / len(self.mean_price_picasso)
            if self.mean_price_rembrandt:
                self.average_winning_rembrandt = sum(self.mean_price_rembrandt) / len(self.mean_price_rembrandt)
            if self.mean_price_vangogh:
                self.average_winning_vangogh = sum(self.mean_price_vangogh) / len(self.mean_price_vangogh)
        

        # This function updates the winning bids for each artist lists
        def update_winning_bids():
            threshold = 200
            # Declare a threshold to try and avoid distorting the average bid price from bots that bid extreme prices
            #... Bots that blow a significant amount of budget on a single painting won't be able to win and skew the average
            if current_round > 0:
                winning_bid = amounts_paid[current_round-1]
                winner = winner_ids[current_round-1]

                # If bid was above threshold, use the remaining budget ratio to place a more realistic bid value into the artists winning bids list
                if winning_bid > threshold:
                    remaining_budget_ratio = bots['bot_unique_id' == winner]['budget'] / 8 - sum(bots['bot_unique_id' == winner]['paintings'].values())
                    winning_bid = 125 + remaining_budget_ratio

                # Append winning bid to correct class array
                if painting_order[current_round-1] == 'Da Vinci':
                    self.mean_price_davinci.append(winning_bid)
                if painting_order[current_round-1] == 'Picasso':
                    self.mean_price_picasso.append(winning_bid)
                if painting_order[current_round-1] == 'Rembrandt':
                    self.mean_price_rembrandt.append(winning_bid)
                if painting_order[current_round-1] == 'Van Gogh':
                    self.mean_price_vangogh.append(winning_bid)


        # Analyses which competitors are near the winning condition
        def competitors():
            # Initialise dictionary for competitors of interest
            competitor_info = {}
            highest_available_bid_ratio = 0

            # Cycle through current list of bots in the auction
            for bot in bots:
                if bot['bot_name'] != 'u5591185':
                    remaining_budget_ratio = bot['budget'] / 8 - sum(bot['paintings'].values())
                    highest_available_bid_ratio = max(highest_available_bid_ratio, remaining_budget_ratio)

                    # Add competitor to competitors list as they have 3 paintings already
                    if sum(bot['paintings'].values()) > 3:
                        competitor_info[bot['bot_name']] = bot['paintings']

            return highest_available_bid_ratio, competitor_info


        # Determines if the bot shouldn't bet on the current painting
        def avoid_bid(current_painting, my_collection):

            bid = False         # default False indicates bid
            two_or_more = 0     # count for number of artists with 2 or more paintings
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
            
            # No avoid bidding conditions met - bid
            return bid


        # Adjust remaining paintings utilities based on my bots current collection
        def update_utiltity(my_collection, look_ahead, competitors_info, average):

            # Create a sliced list that focuses on the next look ahead value of paintings coming in the auction
            paintings_interest = []
            paintings_interest = painting_order[current_round:current_round+look_ahead]
            of_interest = False
            competitors_competing = 0
            competitors_average = 0

            # Obtain frequency of artists in the next 10 paintings and assign weights based on frequency in next 10 paintings
            # Initialize frequency dictionary with all artists and counts set to 0
            frequency = {artist: 0 for artist in ['Da Vinci', 'Picasso', 'Rembrandt', 'Van Gogh']}
            for artist in paintings_interest:
                frequency[artist] += 1

            # Calculate weights for painting based on frequency of artist in the look ahead period
            weights = {artist: max(0, (look_ahead  / max(1,frequency[artist])) / look_ahead) for artist in set(frequency)}
            
            artists = ['Da Vinci', 'Picasso', 'Rembrandt', 'Van Gogh']
            # Remove current painting from artists
            artists.remove(current_painting)

            # Check whether any competitors (current collection over threshold) will be interested in the current painting
            for bot_name, bot_info in competitors_info.items():
                of_interest = False
                if bot_info[current_painting] < 1 or bot_info[current_painting] == 2:   # If the competitor bot does not have this painting or has 2 is of interest
                    of_interest = True
                if bot_info[current_painting] == 1:                                     # if the competitor has 1 of the current painting
                    safety_lock = 0                                                     # intialise check count
                    for artist in artists:                                              # loop through each remaining artist
                        if bot_info[artist] > 1:                                        # if they have more than one painting from other artist
                            safety_lock += 1                                            # increment safety lock
                    if safety_lock >= 2:                                                # if they already have 2 paintings from 2 other artists
                        of_interest = False                                             # this painting shouldn't be of interest to them
                    else:
                        of_interest = True                                              # Otherwise this painting is of interest
                # if the painting is of interest, increment competitors list for current painting and work out average winning bid of competitors
                if of_interest:
                    competitors_competing += 1
                    competitors_average +=  (((1001 - bots['bot_name' == bot_name]['budget']) / sum(bots['bot_name' == bot_name]['paintings'].values())) + competitors_average ) / competitors_competing

            # Adjust bid vased on whether there are competitors that also need this bid for their collection
            #... this avoids overbidding for paintings that are not of interest to other competitors
            #... and underbidding for desired collections
            if competitors_competing > 0:
                bid = min(competitors_average + 1, min(135, 125 * (1 + (weights[current_painting] / look_ahead))))
            else:
                bid = min(average, 125 * (1 - (weights[current_painting] / (look_ahead / 2))))

            # If we are in a state where we need to increment our collection by 1 (at least 3 artists in the collection have 1 or less paintings)
            #...we check the frequency of the current painting in the next 10, if it only appears 2 or less times, and
            #...the other paintings are also required, we avoid bidding as we look to complete the collection as quickly as possible
            if my_collection[current_painting] == 1:
                avoid = 0
                for artist in artists:                                  # Check whether another artist is also low frequency
                    if my_collection[artist] == 1:
                        avoid += 1
                if frequency[current_painting] <= 2 and avoid >= 2:     # If we have 1 painting from 2 or more artists, we skip the current painting
                    return 0                                            # return 0 to skip, as we do not want to bid for low frequency painting
                    

            # If we do not own any paintings, bid slightly above the average to try ensure our collection begins              
            artists.append(current_painting)
            early_bid = 0
            if competitors_competing < 1:
                for artist in artists:
                    if my_collection[artist] == 0:
                        early_bid += 1
                if early_bid <= 4 and my_collection[current_painting] == 0:
                    bid = 126

            # Return adjusted bid for this round
            return bid
        

        # Decide the best value bid for the current painting
        def decide_bid_value(average, competitors_info):
            # Decide the best bid value based on all the information we have for auction so far
            bid = update_utiltity(my_collection, 10, competitors_info, average)
            
            # If last painting needed for winning condition, bet max remaining budget
            if sum(my_collection.values()) == 7:
                bid = my_bot_details['budget']

            return bid


        # Master function to determine amount to bid on current painting
        def create_bid(current_painting, my_collection):

            # Update the class artist winning bid lists
            update_winning_bids() 
            # Update average winning bid values for each artist
            update_average_bid()

            # Check if the bot should bid this round based on the current collection
            if (avoid_bid(current_painting, my_collection)):
                return 0
            
            # Assess competitors in the auctions current stance
            highest_available_bid_ratio, competitors_info = competitors()

            # get current average bid for current artist and frequency 
            winning_frequency, average = return_frequency_average(current_painting)
            if average == 1:
                average = self.utility[current_round-1]

            # Decide the bid value for this round
            bid = decide_bid_value(average, competitors_info)

            # If bid is higher than remaining budget - bid remaining budget to avoid 0 bid
            if bid > my_bot_details['budget']:
                bid = my_bot_details['budget']

            return bid
        
            
        #print("\n\nMY BOT {}".format(my_bot_details['paintings']))
        #print("\nRemaining Budget: {} \n".format(my_bot_details['budget']))
        
        # Initialise my current collection of paintings variable and determine the bid for this round
        my_collection = my_bot_details['paintings']
        bid = create_bid(current_painting, my_collection)
        #print("MY BID: {}\n\n".format(bid))
        return bid
