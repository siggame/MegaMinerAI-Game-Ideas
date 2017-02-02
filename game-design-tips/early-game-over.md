# Game Design: Early Game Over

This bullet may seem obvious, but it is important none the less.  Often in games we design you can determine a maximum bound on an AI's final score given the current state of the game.  Using that prediction you can determine if that AI can possibly win.  If they can't, don't make everyone sit around and watch more turns for no reason.

### Example: MegaMinerAI 8: BotNet
In this game, at even intervals the player who controlled the most territory was awarded one point.  Whoever has the most points at the end of the game wins.  As such, if the number of remaining points to be awarded was less than the difference in the players' scores, the game was terminated immediately.

### Benefits
Ending the game early has a number of benefits.  First, it makes watching games more interesting, as games only last as long as they need to.  Blow outs end quickly while even games run longer.  This also saves on arena time since fewer turns need to be played.  Finally it provides a simple "interestingness" metric for choosing which games to visualize: longer games are more interesting.

An as of yet unrealized benefit of this method is that you can add a measure of nearness to game over to both the AI interface and visualization.  This could allow teams to change up strategy if they realize their opponent is about to win.  For visualization, it can add to the thrill of the close call, as a team just barely stays alive.

### Word of Caution
Only end a game if you are **certain** the winner is known.  While it may be tempting to say things like "it is unlikely for someone to come back" this is a great way to really piss off competitors.  Even if you are right, they will argue they might have come back if not for your ending the game.  As such you must be mathematically certain the game is over before you end the game early.
