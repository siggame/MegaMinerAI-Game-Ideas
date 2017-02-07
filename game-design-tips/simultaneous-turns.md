# Simultaneous turns

Turn based games can be done in two ways: Round based, or Simultaneous.

## Round Based

This is what you probably think of when thinking of a turn based game. Think Chess. During a "round" each player takes a turn. So Player 1 takes his turn and during that Player 2 can do nothing but wait. Then when they finish Player 2 takes their turn in the round, and Player 1 must wait, etc.

## Simultaneous

With this method there is no concept of a "round", instead each turn all Players plot in secret for what action(s) they will perform. Think Rock-Paper-Scissors. All players choose their hand, then reveal at the same time. Because of this **all simultaneous turn based games are also hidden information games**. This is because if you and your opponent both choose an action, you _must_ hide that, otherwise a smart AI will just wait to see what the other(s) do, in which case they've all deadlocked.

### Hidden Information

Hidden information is complex for two main reasons:

1. When players lack information, and then gain it, it can feel random
2. Determining the outcome of actions if chosen actions conflict

The first point is pretty intuitive. If you have a fog of war type game, and then you get hit by some hidden unit, it feels like you are randomly taking damage. So AIs tend to wander around aimlessly until they have most of the game state to draw conclusions from.

The second point is the main drawback for simultaneous turns.

Consider this, two different players have units next to each other. During their simultaneous turn they choose to move to the same tile. Who ends up on that tile? If both their actions are equally valid then it's not fair to put on there over the other, so you have to build in a mechanic to tell them "Hey you action looked valid at the time, but it turns out it was not. sorry". This is a direct contraction of [preferring deterministic- decisions](deterministic-decisions.md) because the server cannot determine the outcome of an action until both players end their turn, and the clients have even more information hidden.

So, if you do want to do simultaneous turns, try to build in mechanics so that these timing conflicts cannot happen. Perhaps units can only move onto tiles owned by their team, and tile ownership cannot change mid turn, so both sides know for sure where they can/cannot move.
