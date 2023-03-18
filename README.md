# Fuseball tournament tracker

A tracker to calculate the rating of each player in the local fuseball tournament. Calculations are based on the Elo rating. Points are assigned or deducted based on the weighted average which depends on the score difference.
The tracker provides statistics per player and tournament rankings.

How to use:
1. Install [Python](https://www.python.org/). *For example, run `winget install python` in your PowerShell if you are running Windows.*

2. Clone this repository by running in your command line:
```
git clone https://github.com/framesfree/BFtracker.git
```

3. Add your matches to the `scores.scv` in the following format:

```
Player1,Player2,Player3,Player4,Score1,Score2
```
Where `Player1` and `Player2` are in the **Team 1** and `Player3` and `Player4` are in the **Team 2**.

4. Run the script:

```
python3 main.py
```
The script will calculate and output the ratings and log personal development for every player in an xlsx file in the `player_stats` folder.

Here is the typical console output:

![image](https://user-images.githubusercontent.com/1450852/226075025-731c6096-ed64-43f1-8e54-319ffd0e8bfe.png)

## Todo:

- [ ] Change the input file from CSV to XLSX
- [ ] Adjust Elo factor according to user prompt
- [ ] Improve performance