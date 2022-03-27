""" Module for test Blackjack method and functions """
from blackjack import Card, Deck, Player


def test_card_generate():
    """ Test card generator """
    card = Card('\u2665', '2')
    assert card.color == '♥'


def test_card_representation():
    """ Test view card representation """
    card = Card('\u2660', 'A')
    assert repr(card) == 'A♠'


def test_deck_generate():
    """ Test deck generator """
    my_deck = Deck()
    assert len(my_deck.deck) == 52


def test_deck():
    """ Deck generation validation test """
    card_colors = ['\u2660', '\u2665', '\u2666', '\u2663']
    my_deck = Deck()
    my_cards = [(my_card.face, my_card.color)
                for my_card in my_deck.deck
                ]
    for color in card_colors:
        heart_cards = [my_card for my_card in my_cards if my_card[1] == color]
    assert len(heart_cards) == 13


def test_shuffle():
    """ Test shuffle deck """
    my_deck = Deck()
    new_deck = my_deck.deck[:]
    my_deck.shuffle_deck()
    assert my_deck != new_deck


def test_deck_after_gimme_card():
    """ Test for check card in deck, and taken card """
    my_deck = Deck()
    last_card = my_deck.deck[-1]
    my_card = my_deck.gimme_card()
    assert last_card == my_card


def test_deck_couter_after_gimme_card():
    """ Test for check number cards in deck after take card """
    my_deck = Deck()
    my_card = my_deck.gimme_card()
    assert len(my_deck.deck) == 51
    assert my_card not in my_deck.deck


def test_check_points():
    """ Test counting user points """
    player = Player()
    player.cards.append(Card('\u2660', 'Q'))
    player.cards.append(Card('\u2666', 2))
    player.cards.append(Card('\u2663', 3))
    assert player.check_points() == 15


def test_check_points_two_aces():
    """ Test counting two aces only points """
    player = Player()
    player.cards.append(Card('\u2660', 'A'))
    player.cards.append(Card('\u2666', 'A'))
    assert player.check_points() == 21


def test_check_points_one_aces_three_cards():
    """ Test counting cards with one ace """
    player = Player()
    player.cards.append(Card('\u2660', 'K'))
    player.cards.append(Card('\u2666', '6'))
    player.cards.append(Card('\u2666', 'A'))
    assert player.check_points() == 17
