'''
let's assume the scores are in range 0 to 50


just like how the chess rating system takes a reference point that..
if the rating difference is 400, the probability of the higher rated player
winning is 10 times more, we can take a reference in this game

setting benchmark of scores for this demo game:

300: 1400 elo
200: 1000 elo
100: 600 elo
0: 200 elo
'''
import json

with open('example_1.json','r') as f:
    my_dict = json.load(f)

# returns JSON object as a dictionary
print(my_dict)

#calculate elo rating based on the metrics mentioned above
def rating(score):
    elo_rating = 200 + (4*score)
    return elo_rating

def matching(PlayerA):
    my_dict1 = my_dict
    player_a_rating = rating(my_dict[PlayerA])
    #initializing new dictionary that does not contain playerA
    lowest_diff = 1
    best_opponent = ''
    for player in my_dict1:

        prob_a = 1 / (1 + 10 ** ((rating(my_dict1[player]) - player_a_rating) / 400))
        prob_b = 1 - prob_a
        if prob_b >= prob_a and prob_b - prob_a < lowest_diff and player != PlayerA:
            # the players whose probabilities of winning are almost equal is the ideal matching
            lowest_diff = abs(prob_b - prob_a)
            best_opponent = player

    if best_opponent == '':
        highest = 0
        highest_player = ' '
        for player_ in my_dict1:
            if my_dict1[player_] > highest:
                highest = my_dict1[player_]
                highest_player = player_

        second_highest = ' '
        second_highest_score = 0
        for player in my_dict1:
            if highest > my_dict1[player] >= second_highest_score:
                second_highest = player
                second_highest_score = my_dict1[player]

        best_opponent = second_highest

        #print(highest)
      #  print(second_highest)
    best_opponent_rating = rating(my_dict[best_opponent])
    ProbabilityA = 1 / (1 + 10 ** ((best_opponent_rating - player_a_rating) / 400))
    ProbabilityB = 1 - ProbabilityA

    print(f'The best opponent for {PlayerA} is {best_opponent}')
    print(f"Probability of {PlayerA} winning is {ProbabilityA}")

    print(f"if {PlayerA} wins, {PlayerA} 's  rating will increase by {round(32*(1-ProbabilityA), 1)}")
    print(f"if {PlayerA} loses, {PlayerA} 's  rating will decrease by {round(32 * (ProbabilityA), 1)}")


        #formula to calculate probability of player A winning
def findAmatch():

    exit = False
    while not exit:
        player_name = input('Enter Player Name [type exit to break the loop]')

        if player_name != 'exit':
            player_score = int(input('Enter Player score'))
            my_dict[player_name] = player_score
            matching(player_name)
            my_dict.update({player_name : player_score})
            print(my_dict)

            with open('example_1.json','w') as f:
                json.dump(my_dict, f)

        else:
            exit = True




#with open('example_1.json','r') as f:
   # my_dict1 = json.load(f)


findAmatch()
