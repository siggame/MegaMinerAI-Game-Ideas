# Game Design: Soft Walls Get Ignored

If a wall is destructible, it will be destroyed rather than pathed around. If a wall does damage or debuffs a unit pathing through it, then competitors will accept the damage/debuff rather than path around. Destructible walls and penalty walls are both "soft". A "hard" wall is indestructible and blocks pathing.

Competitors have a limited amount of time to produce an AI. During the competition, every competitor has a prioritized list in their head. They know what task they are working on right now, and they have a pretty good idea of what task they are working on next. Their first set of tasks addresses what they NEED, their second set of tasks addresses what they think will HELP THE MOST. "Write a real pathfinder and figure out how to handle bottlenecks" is a complex task that will take some time. If it's not a NEED, then it isn't going to happen during their first set of tasks. During the NEED phase, soft walls will get ignored because they can be. During the HELP THE MOST phase, soft walls will get ignored because competitors are now reacting to what they have seen in the arena, and what they have seen is everyone else ignoring the soft walls.

If walls are soft, they might as well not exist because they will be ignored. 

If walls are hard, then they enforce the need for pathing, and become the single biggest hurdle for competitors to overcome, and the game should be designed with that in mind.
