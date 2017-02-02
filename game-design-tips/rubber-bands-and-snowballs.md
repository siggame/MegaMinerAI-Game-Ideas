# Game Design: Rubber Bands and Snowballs

**Rubber Band**: A game mechanic that _helps_ players when they are losing and _hurts_ players when they are winning.  Think of blue shells in Mario Kart.

**Snowball**: A game mechanic that _hurts_ players when they are losing and _helps_ a players when they are wining.  Think of interest rates on loans / debts.

When designing a game, it is critical that you avoid mechanics that help winners continue to win.  In the extreme case these can make the only strategy a rush.  Consider MegaMinerAI 2: Elements.  In this game most resource existed in the middle of the map.  Resource was used to buy more units.  Therefore if you gained control of the middle first, you get more resources to help you hold the middle.  In this way a small lead (winning the first clash) turns into a larger one.  Just by winning the first clash you by definition have more living units.  By the time your opponent regroups, you have been able to gather more resource than your opponent has access to, allowing you to build even more units.  Combined with your original survivors and the fact that you were good enough to win the first clash, its almost impossible for your opponent to recover.

We saw a very similar problem in MegaMinerAI 5: Bloom.  In this game the more territory you controlled, the more resource you got to spend on getting more territory.  Therefore if you got a small lead in controlled area, it was much easier to gain even more area.

Most games have some amount of snowball.  If you kill an opponents unit, then in future combat you will have more units than them.  It can even be intentional, as it means smart decisions early can help you win later.  What matters is how strong the effect is.  You should win because you played smart the whole game, not just that you were smart in the first few decisions.

Rubber bands are a good way to overcome this problem.  For example in MegaMinerAI 8: BotNet we made unit resources a rubber band.  The more units you had alive in the game, the less resources you got per turn to spend on resources.  This means even if all of you units died without killing a single opponent unit, you had a chance at a comeback.

The usual fear in rubber bands is that they make it beneficial to play poorly for a time, with only the last few turns mattering.  This is were decoupling your victory condition from your ability to compete with your opponent.  In BotNet you earned points each turn that were independent of your resources.  Therefore killing an opponent's unit can allow you to earn more points then them for a time, but not forever.  So its always in your best interest to kill an opponent's unit, but it doesn't win you the game.

Rubber bands help keep games interesting and allow late game decisions to have more impact on who wins.  Most games will have snowballs built in without you even trying, so when adding mechanics, its much better to intentionally add a rubber band than a snowball.
