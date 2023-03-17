# Baby Foot tournament tracker
With Elo rating system

How to use:
1. Install [Python](https://www.python.org/). *For example, `winget install python` in your PowerShell if you are running Windows.*

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
The script will calculate and output the ratings and log personal development for every player in a separate csv file in the `player_stats` folder.

Here is the typical console output:

![image](https://user-images.githubusercontent.com/1450852/226056017-2c04248d-a958-4941-9fb7-cfe5a5ccf79e.png)
