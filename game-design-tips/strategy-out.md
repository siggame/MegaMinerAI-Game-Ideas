# Game Design: Strategy Out

The best way to explain the difference between these two concepts is by analogy. **Strategy Up** is like building a tower, while **Strategy Out** is like building a mall.

In a Strategy Up game competitors will write a single strategy which they iteratively refine.
There isn't much choice in the order they make the improvements, as each has to build on the previous. If they are having trouble getting something to work right, or can't figure out what the next step is, they can get frustrated. Consider a game where there is a single type of unit and a single way for that unit to earn you points (BotNet). The game then consists of finding better and better ways of controlling that type of unit, with little diversity in ways to improve an existing AI.

In a Strategy Out game competitors will iteratively add separate components to their strategy. Which one they start with doesn't matter as the individual parts don't rely on each other terribly. If a competitor is having trouble with a specific component, they can always stop and work on something else. Consider a game where you have multiple useful types of units that require different control methods (Space). Your AI will eventually need to know how to control all types of units, but which one you work on improving is up to you.

Note that having multiple unit types is only Strategy Out if the way in which those types need to act is different. Also, Strategy Out can be achieved even with a single type of unit if there is sufficient goal diversity.
