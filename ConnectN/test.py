
import random
import game
import agent
import alpha_beta_agent as aba

# Set random seed for reproducibility
random.seed(1)

wins = 0
games = 10
for i in range(games):
    #
    # Random vs. Random
    #
    # g = game.Game(7, # width
    #               6, # height
    #               4, # tokens in a row to win
    #               agent.RandomAgent("random1"),       # player 1
    #               agent.RandomAgent("random2"))       # player 2

    #
    # Human vs. Random
    #
    # g = game.Game(7, # width
    #               6, # height
    #               4, # tokens in a row to win
    #               agent.InteractiveAgent("human"),    # player 1
    #               agent.RandomAgent("random"))        # player 2

    #
    # Random vs. AlphaBeta
    #
    g = game.Game(6, # width
                  7, # height
                  4, # tokens in a row to win
                  aba.AlphaBetaAgent("bad", 1),          # player 1
                  aba.AlphaBetaAgent("alphabeta", 3)) # player 2

    #
    # Human vs. AlphaBeta
    #
    # g = game.Game(7, # width
    #               7, # height
    #               4, # tokens in a row to win
    #               agent.InteractiveAgent("human"),    # player 1
    #               aba.AlphaBetaAgent("alphabeta", 4)) # player 2

    #
    # Human vs. Human
    #
    # g = game.Game(7, # width
    #               6, # height
    #               4, # tokens in a row to win
    #               agent.InteractiveAgent("human1"),   # player 1
    #               agent.InteractiveAgent("human2"))   # player 2

    # Execute the game
    outcome = g.go()

    if (outcome) == 2:
        wins += 1

print("Final Winrate: ", wins/games)
