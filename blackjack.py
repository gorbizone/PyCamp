# -*- coding: utf-8 -*-
""" Blackjack - card game simulator """
from random import shuffle

BANNER = """
 ######  #          #     #####  #    #       #    #     #####  #    # 
 #     # #         # #   #     # #   #        #   # #   #     # #   #  
 #     # #        #   #  #       #  #         #  #   #  #       #  #   
 ######  #       #     # #       ###          # #     # #       ###    
 #     # #       ####### #       #  #   #     # ####### #       #  #   
 #     # #       #     # #     # #   #  #     # #     # #     # #   #  
 ######  ####### #     #  #####  #    #  #####  #     #  #####  #    #             
"""


class PointsExceed(Exception):
    """ Exception when player exceed 21 points """


class UserPointsExceed(Exception):
    """ Exception when user:Player exceed 21 points """


class CroupierPointsExceed(Exception):
    """ Exception when croupier:Player exceed 21 points """


class Card:
    """ Card definitions """
    colors = ['\u2660', '\u2665', '\u2666', '\u2663']
    faces = list(range(2, 11)) + ['J', 'Q', 'K', 'A']

    def __init__(self, color, face):
        self.color = color
        self.face = face

    def __repr__(self):
        return f'{self.face}{self.color}'


class Deck:
    """ Deck definitions containing 52 cards:Card instances """

    def __init__(self):
        self.deck = [Card(color, face) for face in Card.faces
                     for color in Card.colors]

    def shuffle_deck(self):
        """ Deck shuffle before play """
        shuffle(self.deck)

    def gimme_card(self):
        """ Pulls a card from the deck """
        return self.deck.pop(-1)


class Player:
    """ Player class definition """
    def __init__(self):
        self.cards = []

    def check_points(self):
        """ Check player points """
        points = 0
        num_of_aces = len([card for card in self.cards if card.face == 'A'])

        if num_of_aces == 2 and len(self.cards) == 2:
            return 21

        if num_of_aces == 1 and len(self.cards) == 2:
            points = 10

        for card in self.cards:
            if card.face == 'A':
                points += 1
            elif card.face in ['J', 'Q', 'K']:
                points += 10
            else:
                points += int(card.face)

        if points > 21:
            raise PointsExceed

        return points

    def collect_card(self, card):
        """ Take card from deck """
        self.cards.append(card)


class Game:
    """ Main play logic definition """
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()

    @staticmethod
    def _show_menu():
        print(BANNER)
        print('You see below Your cards. What do You want to do?')
        print('1 - Take next card ; 2 - Stop playing\n')

    def _user_play(self):
        self._show_menu()
        user = Player()
        for _ in range(2):
            user.collect_card(self.deck.gimme_card())
        while True:
            print(f'User cards: {user.cards}, {user.check_points()}')
            choice = input('Waiting for choice: ')
            if choice == '1':
                user.collect_card(self.deck.gimme_card())
            elif choice == '2':
                return user.check_points()
            else:
                print('Wrong option!')

    def _croupier_play(self, user_points):
        croupier = Player()
        for _ in range(2):
            croupier.collect_card(self.deck.gimme_card())

        while croupier.check_points() < user_points:
            croupier.collect_card(self.deck.gimme_card())
        print(f'Croupier cards: {croupier.cards}, {croupier.check_points()}')

        return croupier.check_points()

    def play(self):
        """ Start playing game """
        try:
            user_points = self._user_play()
        except PointsExceed as error:
            raise UserPointsExceed from error

        try:
            self._croupier_play(user_points)
        except PointsExceed as error:
            raise CroupierPointsExceed from error

        print('Croupier WIN in Play!')


if __name__ == '__main__':
    try:
        game = Game()
        game.play()
    except CroupierPointsExceed:
        print('User WIN! Croupier exceeded 21 points.')
    except UserPointsExceed:
        print('Croupier WIN! User exceeded 21 points.')
