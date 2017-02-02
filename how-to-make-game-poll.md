# How to make the game poll

## Google Form Setup

For each MegaMinerAI, we can easily do a fair ballot.

To do so, first go to the SIG-Game Google Drive, and open the Google Form at `SIG-Game Archive/General/MegaMinerAI ## Game Poll`

Make a copy of that to `SIG-Game Archive/## - GAME_NAME/Polls/MegaMinerAI ## Game Poll`, where you replace `##` and `GAME_NAME` with the number and game name respectively.

Make sure to change all the games in there from `GAME_#` to their name, and update the github links to the game ideas.

For the bottom section you'll need to ensure there is a number for every game, so if you had games:

[ Chess, Checkers, Go, Warcraft, Statecraft, Civ ]

you'd need the numbers

[ 1st, 2nd, 3rd, 4th, 5th, 6th ]

and so on.

Then send out the ballot. Google Forms thankfully randomizes the order for fairness. For the game links I recommend alphabetical order.

# Counting Ballots

Once they are in export the results to a google spreadsheet. Then open that spreadsheet in google docs.

Once in the spreadsheet, click File -> Download As -> CSV

Now with that file overwrite the `data.csv` file alongside this file. You'll notice the `game-voter.py` script in this repo. It will read in that `data.csv` file, and output a string you can use to get the results.

Run the script via `python3 game-voter.py` and paste the output to http://www.cs.wustl.edu/~legrand/rbvote/calc.html

Then click "Calculate all winners", and see who won! It will use a variety of algorithms, and there should be a clear winner. If there is not, let the leads decide.
