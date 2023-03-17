import csv
import os

from tabulate import tabulate
from colorama import Fore, Back, Style

def calculate_elo_rating(winner, loser, winner_score, loser_score):
    K = 50  # constant factor to adjust the weight of each game


    # Compute the expected win probabilities for each player on the winning and losing teams
    winner_expected = 1 / (1 + 10 ** ((loser[0] + loser[1] - winner[0] - winner[1]) / 400))
    loser_expected = 1 / (1 + 10 ** ((winner[0] + winner[1] - loser[0] - loser[1]) / 400))
   

    # Determine the point differential and calculate the corresponding adjustment factor
    point_diff = abs(winner_score - loser_score)
    if point_diff == 5:
        adj_factor = 1
    else:
        adj_factor = 0.2 * point_diff

    # Calculate the elo rating changes for each player on the winning and losing teams
    winner_delta = round(K * adj_factor * (1 - winner_expected))
    loser_delta = round(K * adj_factor * (0 - loser_expected))

    # Update the elo scores for each player on the winning and losing teams
    new_winner_elo = (winner[0] + winner_delta, winner[1] + winner_delta)
    new_loser_elo = (loser[0] + loser_delta, loser[1] + loser_delta)

    # Return the new elo scores for both teams
    return (new_winner_elo, new_loser_elo)


def update_players(players, team1, team2, score1, score2):
    """
    Updates the players' ELO ratings based on match results and returns updated players dictionary.
    """
    winner1, winner2 = team1 if score1 > score2 else team2
    loser1, loser2 = team2 if score1 > score2 else team1
    new_winner_elo, new_loser_elo = calculate_elo_rating((players[winner1],players[winner2]), (players[loser1],players[loser2]), score1,score2)
    
    players[winner1] = new_winner_elo[0] if new_winner_elo[0] > 0 else 0
    players[winner2] = new_winner_elo[1] if new_winner_elo[1] > 0 else 0
    players[loser1] = new_loser_elo[0] if new_loser_elo[0] > 0 else 0
    players[loser2] = new_loser_elo[1] if new_loser_elo[1] > 0 else 0
    
    # Write point history of each player to CSV file
    for player in [winner1, winner2, loser1, loser2]:
       filename = f"player_stats/{player}_history.csv"
       with open(filename, "a", newline="") as csvfile:
           writer = csv.writer(csvfile)
           writer.writerow([players[player]]) 
    return players


def print_ranking(players):
    """
    Prints the player rankings in the order of ELO rating, from highest to lowest.
    """
    ranking = sorted(players.items(), key=lambda x: x[1], reverse=True)
    headers = ["Rank", "Player", "Points"]
    rows = []
    for i, (player, points) in enumerate(ranking, start=1):
        rank = f"{i}"
        rows.append([rank, player, round(points)])
    
    table = tabulate(rows, headers=headers, tablefmt="fancy_grid", numalign="center", stralign="center")
    
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + table + Style.RESET_ALL)


def main():
    players = {}  # initialize an empty dictionary to store player names and ELO ratings

# Create directory if it doesn't exist
    if not os.path.exists('player_stats'):
     os.makedirs('player_stats')

    with open("scores.csv") as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip the first row
        for row in reader:
            if len(row) >= 6:
                team1 = row[0], row[1]
                team2 = row[2], row[3]
                score1, score2 = int(row[4]), int(row[5])
                for player in team1 + team2:
                    if player not in players:
                        players[player] = int(1000)  # initialize new player's score to 1000
                players = update_players(players, team1, team2, score1, score2)
    
    print_ranking(players)


# run the program
if __name__ == "__main__":
    main()