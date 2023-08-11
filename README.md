BlackJack-Simulator with Various Card Counting Techniques
==============================================

Augmented from: https://github.com/seblau/BlackJack-Simulator

### Running
At the bottom of `tester.py` comment in or out whichever simulations you'd like to run. Then run

    python tester.py

This is one example counting technique
Omega II Count:

| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | J | Q | K | A |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +1 | +1 | +2 | +2 | +2 | +1 | 0 | -1 | -2 | -2 | -2 | -2 | 0 |

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