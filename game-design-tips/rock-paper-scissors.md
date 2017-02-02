# Game Design: Rock, Paper, Scissors

AI is about decision making. In a game, either there is a decision that always wins (a dominant strategy) or every decision is beaten by another decision (there is a rock-paper-scissors). When there is a dominant strategy, that means there are no decisions to be made: an AI that employs the dominant strategy will beat any AI that doesn't. With rock-paper-scissors, many different strategies can be valid, and the best AIs will be able to execute many strategies and switch between them.

The easiest way to get rock-paper-scissors into games is to look at all the different decision points we might have, and intentionally introduce a rock-paper-scissors relationship into them.

# Example Rock-Paper-Scissors
## MegaMiner examples
### Fast-Strong-Ranged
Perhaps the most standard RPS relation in MegaMiners:

The ranged unit beats the strong unit by kiting or getting enough shots to win before the strong guy can reach it.

The fast unit beats the ranged unit by being able to close the distance quickly enough to get at the ranged unit's creamy center.

The strong unit beats the fast unit by hitting it really hard if it dares to get close.

This is also an interesting relationship because all three unit types need to be played somewhat differently to maximize their effectiveness, and can favor different map terrain layouts.
### Splash-Heavy-Cheap
A unit that can attack many units a turn beats cheap units by being able to damage many at once.

A heavy hitting unit beats a splash unit by having comparably superior defense and offense in a 1 on 1 match.

Cheap units beat a heavy unit by being able to attack it many times together while it can only remove one of them per turn.

### Tech-Mixed-Rush
A team that focuses on researching better units can out compete a team that spends some resources making units.

A team that balances unit purchasing and upgrading can survive against a team that doesn't upgrade long enough to win.

A team that spends all of their resources on units can overpower a team which only focuses on research before their plans come to fruition.

### Expensive-Cheap-[[Stun|stunner]]
A [[stunner]] unit is a unit whose attack rather than damage an enemy denies its next turn.

Stunners can beat expensive units by effectively being able to "cancel out" a unit that cost more to make.

Cheaper units beat stunners because the stunner can only stop one unit that costs less than itself to make.

## Non-MegaMiner (yet!) examples.
### Fire-Water-Grass
Pokémon contains at least 15 different rock-paper-scissors relations between its 18 types. This combined with the 6 party slots and opportunities for a Pokemon to have moves of other types gives many options and incentives for party diversification, and to allow many types of Pokemon with meaningful differentiation.

### Break Over Point RPS
Unlike other versions, this RPS deals with group composition.  Consider a two unit game, healers and archers.  Under a certain number of archers, adding more healers makes them better, IE 6:4 > 7:4 > 8:2 > 9:1, where the first number is archers and the second number is healers.  But given enough archers you start getting the ability to kill a healer (or archer) in a single turn, nullifying healers entirely.