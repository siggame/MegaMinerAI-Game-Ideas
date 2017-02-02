# Game Design: Deterministic Decisions

Writing an AI is all about decision making.  In a game were there are no decisions, there is no AI.  In a game where the outcome of all decisions are completely unknown, there is still no AI.  Its the decisions where you can make the right and wrong choice that really matter.  The problem is that when the outcome of a decision is stochastic, you can't know if a decision was good or bad before you made it.

Consider a low health unit facing a low health opponent.  The opponent has a probability to dodge, causing it to ignore all the damage from a single attack.  If I attack and the opponent dodges, it was a bad idea to stick around as I will likely die next turn without accomplishing anything.  Should have run.  But if I attack and the opponent fails to dodge, I can kill them and survive the clash.

In this case, the "right" choice can't be made every time.  Yes a top notch player can play the odds, but this is a 24 hour competition.  Players determine strategy by guess work and a minimal amount of watching games.  If they get lucky being overly aggressive in the game they watch, they will likely do that forever.

Another point to consider as well.  Chance allows good players to lose to bad players because someone got "lucky" or "unlucky."  If we want a game that rewards people for playing well, why would we want mechanics that rewards people for playing lucky?
