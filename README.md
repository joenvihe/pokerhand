# Pokerhand

Create the class PokerHand with the following variables and methods:
- Variables:
    - cards: String with the pokerhand
    - lst_denominations: Represent the numbers of the cards
    - lst_suits: Represent the suits of the cards
- Methods:
    - split_hand: generate the variables lst_denominations and lst_suits
    - isConsecutive: determines if the numbers in the hand are consecutive with no duplicates
    - is_royal_flush: return True if poker hand is royal flush, also the max value of royal flush card's
    - is_straight_flush: return True if poker hand is straight flush, also the max value of straight flush card's
    - is_four_kind: return True if poker hand is four of a kind, also the max value of card's four of a kind
                    and sum values of the  others card's
    - is_full_house: return True if poker hand is full house, also the max value of card's full house
                    and sum values of the  others card's
    - is_flush: return True if poker hand is flush, also sum values of the  card's flush
    - is_straight: return True if poker hand is straight, also sum values of the  card's straight
    - is_three_kind: return True if poker hand is three of a kind, also the max value of card's three of a kind
                    and sum values of the  others card's
    - is_two_pair: return True if poker hand is two pair, also the sum value of card's two pair
                    and sum values of the  others card's
    - is_one_pair: return True if poker hand is one pair, also the max value of card's one pair
                    and sum values of the  others card's
    - get_strong_and_val_max: Identifi the PokerHand and give a weigth, also return de sum values of Poker Hand
    - compare_with: Compare two porkerhands return "WIN" or "LOSS"
