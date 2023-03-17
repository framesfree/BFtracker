# Baby Foot tornament tracker
With Elo rating system

How to use:
1. Install Python.
*For example, `winget install python` in your PowerShell if you are running Windows*
2. Clone this repository by running in your command line:
```
git clone https://github.com/framesfree/BFtracker.git
```
3. Add your matches to the 'scores.scv' in the following format:
```
Player1,Player2,Player3,Player4,Score1,Score2
```
Where `Player1` and `Player2` are in the Team 1 and `Player3` and `Player4` are in the Teamm 2.
4. Run the script:
```
python main.py
```

The script will calculate and output the ratings and log personal development for every player in a separate csv file in the `player_stats` folder.