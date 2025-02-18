BlackJack-Simulator with Various Card Counting Techniques
==============================================

Augmented from: https://github.com/seblau/BlackJack-Simulator to handle more card counting techniques and to do deeper statistical analytics.

### Running
At the bottom of `tester.py` comment in or out whichever simulations you'd like to run. Then run

    python tester.py

Some example counting methods are below:

|Counting method | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | J | Q | K | A |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Omega II | +1 | +1 | +2 | +2 | +2 | +1 | 0 | -1 | -2 | -2 | -2 | -2 | 0 |
HI LO | +1 | +1 | +1 | +1 | +1 | 0 | 0 | 0 | -1 | -1 | -1 | -1 | -1 |
HI OPT I | 0 | +1 | +1 | +1 | +1 | 0 | 0 | 0 | -1 | -1 | -1 | -1 | 0 |
HI OPT II | 0 | +1 | +2 | +2 | +1 | +1 | 0 | 0 | -2 | -2 | -2 | -2 | 0 |
HALVES | +0.5 | +1 | +1 | +1.5 | +1 | +0.5 | 0 | -0.5 | -1 | -1 | -1 | -1 | -1 |
RED SEVEN | +1 | +1 | +1 | +1 | +1 | +0.5 | 0 | 0 | -1 | -1 | -1 | -1 | -1 |
ZEN | +1 | +1 | +2 | +2 | +2 | +1 | 0 | 0 | -2 | -2 | -2 | -2 | -1 |

So, for example if there is a player-favorable count like +20 by 2 decks remaining, the simulator bets the standard bet times the specified *BET_SPREAD*.

### Definition of Terms

The simulator involves several concepts related to Blackjack game play:
* A *Hand* is a single hand of Blackjack, consisting of two or more cards
* A *Round* is single round of Blackjack, in which one or more players play their hands against the dealer's hand
* A *Shoe* consists of multiple card decks consisting of SHOE_SIZE times 52 cards
* A *Game* is a sequence of Rounds that starts with a fresh *Shoe* and ends when the *Shoe* gets reshuffled

### Result

When comparing the PMF of different card counting strategies, it becomes aparent that they have various distributions depending on how agressive/subtle the counting methodologies are. You can see that some strategies have peaks that are farther right, which is more ideal, i.e. they have a higher expected edge on the dealer. However, these strategies also have a wider and wider variance as the strategies expected edge gets higher and higher. This means that there is higher volatility with these competitive stategies.

![PMF of various card counting strategies](/documentation/PMF_card_counting.png?raw=true)

Another analysis we can do is varying the shoe size. As the shoe size grows, the higher potential for variance in hands, but also the higher potential for taking advantage of a running count.

![Probability distribution of hands won and lost varying nothing but shoe size](/documentation/shoe_size.png?raw=true)

To minimize the advantage of card counting today, casinos implement a maximum shoe depth which limits how many cards deep into a shoe are playable in any given game. After 25% of the shoe is completed for example, the entire shoe might be reshuffled, requiring card counters to start over their counting. Below is an example of how the edge of the Omega II strategy changes with an adjustment of the shoe depth. As the depth is reduced (moving towards the right), establishing an edge gets harder and harder because there are fewer cards a card counter can take advantage of before getting a high count.

![Shoe Depth vs percent edge with the Omega II strategy](/documentation/shoe_penetration.png?raw=true)