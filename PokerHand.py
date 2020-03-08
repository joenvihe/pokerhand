import unittest

"""
Create the class Result with varibles contant to define "WIN" and "LOSS"
"""
class Result():
    WIN = "WIN"
    LOSS = "LOSS"

"""
Create the class TestPokerHandMethods, to test the method compare_with of the class PokerHand
"""
class TestPokerHandMethods(unittest.TestCase):
    def test_pokerhand(self):
        self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5C 5H AC")) == Result.WIN)
        self.assertTrue(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JC AS KC TD")) == Result.LOSS)
        self.assertTrue(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7C JS TS 6D")) == Result.WIN)
        self.assertTrue(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7S 5S 5D JS")) == Result.LOSS)
        self.assertTrue(PokerHand("AS AD KD 7C 3D").compare_with(PokerHand("AD AH KD 7C 4S")) == Result.LOSS)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("AC AH AS AS KS")) == Result.WIN)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JS QC KS AC")) == Result.WIN)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(PokerHand("TC JS QC KS AC")) == Result.WIN)
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JC JS JD TH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4H 5H 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.LOSS)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.LOSS)
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)

"""
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
"""
class PokerHand:
    cards = None
    lst_denominations = None
    lst_suits = None

    # initialize the variables
    def __init__(self, cards):
        self.cards = cards
        self.split_hand()

    # generate the variables lst_denominations and lst_suits
    def split_hand(self):
        # get the lst_denominations, tranform the letters to numbers
        self.lst_denominations = [int(i[0]\
                                      .replace("T","10")\
                                      .replace("J","11")\
                                      .replace("Q","12")\
                                      .replace("K","13")\
                                      .replace("A","14")) for i in self.cards.split(" ")]
        #get the lst_suits
        self.lst_suits = [i[1] for i in self.cards.split(" ")]

    # determines if the numbers in the hand are consecutive with no duplicates
    def isConsecutive(self):
        numbers = self.lst_denominations
        # idenetify not duplicates
        if len(numbers) != len(set(numbers)):
            return False
        # sort the list
        numbers.sort()
        # validate is consecutive
        result = True
        for i,v in enumerate(numbers[:-1]):
            if (numbers[i+1] - v) not in [1,8]:
                result = False
                break
        return result

    # return True if poker hand is royal flush, also the max value of royal flush card's
    def is_royal_flush(self):
        # validate all denominations is in the range 10 to 14
        for i in self.lst_denominations:
            if i not in [10,11,12,13,14]:
                return (False,0,0)
        # validate all have the same suits
        one_suit_val = len(list(set(self.lst_suits)))
        if one_suit_val != 1:
            return (False, 0, 0)
        return (True, 14, 0)

    # return True if poker hand is straight flush, also the max value of straight flush card's
    def is_straight_flush(self):
        # validate only have one suit
        one_suit_val = len(list(set(self.lst_suits)))
        # get sum of all denomination
        val = sum(self.lst_denominations)
        # validate only have one suit and the poker hand is consecutive
        return (one_suit_val == 1 and self.isConsecutive(),val,0)

    # return True if poker hand is four of a kind, also the max value of card's four of a kind
    # and sum values of the  others card's
    def is_four_kind(self):
        # transform the lst_denomination to dictionary
        val_dict = {i: self.lst_denominations.count(i) for i in self.lst_denominations}
        # validate in the dictionary have four equals numbers, get the number and sum the rest numbers
        val, vKey, sumRes = 0, 0, 0
        for key, value in val_dict.items():
            if value == 4 and  len(val_dict) == 2:
                    val = value
                    vKey = key
            else:
                sumRes += key
        # if not exist four equals numbers
        if val != 4:
            return (False, 0,0)
        return (True,vKey,sumRes)

    # return True if poker hand is full house, also the max value of card's full house
    # and sum values of the  others card's
    def is_full_house(self):
        # transform the lst_denomination to dictionary
        val_dict = {i: self.lst_denominations.count(i) for i in self.lst_denominations}
        # validate the length of dictionary is two
        if len(val_dict) != 2:
            return (False,0,0)
        # validate if the poker hand exist only two diferrentes sluts with 2 and 3 cards
        val, vKey, sumRes = 0, 0, 0
        for key, value in val_dict.items():
            if value in [2,3]:
                vKey += key
                val += value
            # get the max value of full house card's
            if key > sumRes:
                sumRes = key
        if val != 5:
            return (False,0,0)
        return (True,vKey,sumRes)

    # return True if poker hand is flush, also sum values of the  card's flush
    def is_flush(self):
        # validate have only one suit
        one_suit_val = len(list(set(self.lst_suits)))
        # sum all numbers of the poker hand
        return (one_suit_val == 1,sum(self.lst_denominations),0)

    # return True if poker hand is straight, also sum values of the  card's straight
    def is_straight(self):
        # return if is consecutive and max value of the poker hands
        return (self.isConsecutive(),max(self.lst_denominations),0)

    # return True if poker hand is three of a kind, also the max value of card's three of a kind
    # and sum values of the  others card's
    def is_three_kind(self):
        # transform the lst_denominations in dictionary
        val_dict = {i: self.lst_denominations.count(i) for i in self.lst_denominations}
        # validate have 3 components
        if len(val_dict) != 3:
            return (False,0,0)
        # validate if a one componet in the dicctionary have 3 equals cards, get the value and sum the rest card's
        val, vKey, sumRes = 0, 0, 0
        for key, value in val_dict.items():
            if value == 3 :
                val = value
                vKey = key
            else:
                sumRes += key
        # validate if a one componet in the dicctionary have 3 equals cards
        if val != 3:
            return (False, 0, 0)
        return (True, vKey, sumRes)

    # return True if poker hand is two pair, also the sum value of card's two pair
    # and sum values of the  others card's
    def is_two_pair(self):
        # transform the lst_denominations in dictionary
        val_dict = {i: self.lst_denominations.count(i) for i in self.lst_denominations}
        # validate have 3 components
        if len(val_dict) != 3:
            return (False,0,0)
        # validate if two component's in the dicctionary have 2 equals cards, get the sum value's and sum the rest card's
        val, vKey, sumRes = 0, 0, 0
        for key, value in val_dict.items():
            if value == 2:
                val += value
                vKey += key
            else:
                sumRes += key
        # not exist two pair
        if val != 4:
            return (False,0,0)
        return (True,vKey,sumRes)

    # return True if poker hand is one pair, also the max value of card's one pair
    # and sum values of the  others card's
    def is_one_pair(self):
        # transform the lst_denominations in dictionary
        val_dict = {i: self.lst_denominations.count(i) for i in self.lst_denominations}
        # validate have 4 components
        if len(val_dict) != 4:
            return (False,0,0)
        # validate if 1 component is one pair, get the value and sum rest card's
        val, vKey, sumRes = 0, 0, 0
        for key, value in val_dict.items():
            if value == 2:
                val = value
                vKey = key
            else:
                sumRes += key
        # not have 1 component or one pair
        if val != 2:
            return (False,0,0)
        return (True,vKey,sumRes)

    # Identifi the PokerHand and give a weigth, also return de sum values of the play win card's and the rest card's
    def get_strong_and_val_max(self):
        vTemp = self.is_royal_flush()
        if vTemp[0]:
            return (10,vTemp[1],vTemp[2])

        vTemp = self.is_straight_flush()
        if vTemp[0]:
            return (9,vTemp[1],vTemp[2])

        vTemp = self.is_four_kind()
        if vTemp[0]:
            return (8,vTemp[1],vTemp[2])

        vTemp = self.is_full_house()
        if vTemp[0]:
            return (7,vTemp[1],vTemp[2])

        vTemp = self.is_flush()
        if vTemp[0]:
            return (6, vTemp[1],vTemp[2])

        vTemp = self.is_straight()
        if vTemp[0]:
            return (5, vTemp[1],vTemp[2])

        vTemp = self.is_three_kind()
        if vTemp[0]:
            return (4, vTemp[1],vTemp[2])

        vTemp = self.is_two_pair()
        if vTemp[0]:
            return (3, vTemp[1],vTemp[2])

        vTemp = self.is_one_pair()
        if vTemp[0]:
            return (2, vTemp[1],vTemp[2])

        return (1,sum(self.lst_denominations),0)

    # Compare two porkerhands return "WIN" or "LOSS"
    def compare_with(self,other_hand):
        # get the strong and value max Pokerhand type's
        val1,valM1,res1 = self.get_strong_and_val_max()
        val2,valM2,res2 = other_hand.get_strong_and_val_max()

        # do the compare
        if ( val1 > val2 ) or \
           ( val1 == val2 and int(valM1) > int(valM2) )  or \
           ( val1 == val2 and int(valM1) == int(valM2) and int(res1) > int(res2) ) :
           return "WIN"
        return "LOSS"

if __name__ == '__main__':
    unittest.main()