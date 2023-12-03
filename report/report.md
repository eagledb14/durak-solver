

# naive

This player gets the best next hand after it plays. So it looks at all the plays that it can do on that turn (whether attack or defense) and sees which move makes its hand look better. 

It sucks, it can't beat the random player most of the time in a 1v1, though when there are more players it never gets last



# naive move

This player looks at the best cards it can play. I had it prioritize plays that included as many cards as possible, and that used lower card costs. So that it would use the worse cards first. A move is also penalized when it uses cards with the trump suit, so that it saves those when it has to use them.

It's actually pretty good. I would say that durak is partially luck based game, so it's not guaranteed to win, but it wins most games (like 70%) against random and naive player in 1v1s and hasn't lost in 4 players. When there are 3 nm players and 1 random or naive player, the random or naive player usually loses, even though it has more chances to lose.
