from should_dsl import should, should_not
import pytest


class Field(object):
    def __init__(self, number_of_players):
        self.players = range(number_of_players)


class Game(object):
    def __init__(self, number_of_players):
        self.field = Field(number_of_players)


def test_have_collection_passed():
    Game(10) | should | have(10).players_on_field


def test_should_not_have_collection_passed():
    Game(10) | should_not | have(11).players_on_field


def test_have_collection_failed():
    Game(10) | should | have(11).players_on_field
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected 11 'players on field', got 10


def test_should_not_have_collection_failed():
    Game(10) | should_not | have(10).players_on_field
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target not to have 10 'players on field', got 10


class Field(object):
    def __init__(self, number_of_players):
        self._players = range(number_of_players)
        self.goals = 2

    def players(self):
        return self._players

    def ball(self):
        return 0


class Game(object):
    def __init__(self, number_of_players):
        self._field = Field(number_of_players)

    def field(self):
        return self._field


def test_have_collection_passed2():
    Game(10) | should | have(10).players_on_field


def test_should_not_have_collection_passed2():
    Game(10) | should_not | have(11).players_on_field


def test_have_collection_failed2():
    Game(10) | should | have(11).players_on_field
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected 11 'players on field', got 10


def test_should_not_have_collection_failed2():
    Game(10) | should_not | have(10).players_on_field
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target not to have 10 'players on field', got 10


def test_should_not_have_collection_failed3():
    Game(10) | should_not | have(1).ball_on_field
    # Traceback(most recent call last):
    #     ...
    # TypeError: target's 'ball()' does not return an iterable


def test_should_not_have_collection_failed4():
    Game(10) | should_not | have(1).goals_on_field
    # Traceback(most recent call last):
    #     ...
    # TypeError: target's 'goals' is not an iterable
