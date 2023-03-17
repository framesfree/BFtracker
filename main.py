import csv
import os

from tabulate import tabulate
from colorama import Fore, Back, Style

def calculate_elo_rating(winner, loser, winner_score, loser_score):
    """
    Calculates new ELO rating for players based on match results and returns updated ELO ratings.
    """
    K = 32  # ELO coefficient
    winner_expected = 1 / (1 + 10 ** ((loser - winner) / 400))
    loser_expected = 1 / (1 + 10 ** ((winner - loser) / 400))
    winner_new_elo = winner + K * (winner_score / 5 - winner_expected)
    loser_new_elo = loser + K * (loser_score / 5 - loser_expected)
    return winner_new_elo, loser_new_elo


def update_players(players, team1, team2, score1, score2):
    """
    Updates the players' ELO ratings based on match results and returns updated players dictionary.
    """
    winner1, winner2 = team1 if score1 > score2 else team2
    loser1, loser2 = team2 if score1 > score2 else team1
    winner_elo = calculate_elo_rating(winner1+winner2, loser1+loser2, score1,score2)
    loser_elo = calculate_elo_rating(winner1+winner2, loser1+loser2, score2,score1)
    
    winner_new_elo1, winner_new_elo2 = calculate_elo_rating(
        players[winner1], players[winner2], score1, score2
    )
    loser_new_elo1, loser_new_elo2 = calculate_elo_rating(
        players[loser1], players[loser2], score2, score1
    )
    players[winner1] = winner_new_elo1 if winner_new_elo1 > 0 else 0
    players[winner2] = winner_new_elo2 if winner_new_elo2 > 0 else 0
    players[loser1] = loser_new_elo1 if loser_new_elo1 > 0 else 0
    players[loser2] = loser_new_elo2 if loser_new_elo2 > 0 else 0
    
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
                        players[player] = 1000  # initialize new player's score to 1000
                players = update_players(players, team1, team2, score1, score2)
    
    print_ranking(players)


# run the program
if __name__ == "__main__":
    main()