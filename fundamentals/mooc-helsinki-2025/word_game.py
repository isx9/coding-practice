import random

VOWELS = 'aeiou'
MOVES = {'rock', 'paper', 'scissors'}
BEATS = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}


class WordGame:
    """Base class for a two-player word game. Subclasses define round_winner."""

    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):  # pylint: disable=unused-argument
        """Return 1 or 2 for the round winner, or 0 for a tie. Random by default."""
        return random.randint(1, 2)

    def play(self):
        """Play all rounds and print the final result."""
        print('Word game:')
        for round_no in range(1, self.rounds + 1):
            print(f'round {round_no}')
            answer1 = input('player1: ')
            answer2 = input('player2: ')

            winner = self.round_winner(answer1, answer2)
            if winner == 1:
                self.wins1 += 1
                print('player 1 won')
            elif winner == 2:
                self.wins2 += 1
                print('player 2 won')

        print('game over, wins:')
        print(f'player 1: {self.wins1}')
        print(f'player 2: {self.wins2}')


def compare(score1: int, score2: int):
    """Return 1 if score1 is higher, 2 if score2 is higher, 0 on a tie."""
    if score1 > score2:
        return 1
    if score2 > score1:
        return 2
    return 0


class LongestWord(WordGame):
    """The longer word wins the round."""

    def round_winner(self, player1_word: str, player2_word: str):
        return compare(len(player1_word), len(player2_word))


class MostVowels(WordGame):
    """The word with more vowels wins the round."""

    def round_winner(self, player1_word: str, player2_word: str):
        vowels1 = sum(1 for char in player1_word.lower() if char in VOWELS)
        vowels2 = sum(1 for char in player2_word.lower() if char in VOWELS)
        return compare(vowels1, vowels2)


class RockPaperScissors(WordGame):
    """Classic rock-paper-scissors. An invalid move loses to a valid one."""

    def round_winner(self, player1_word: str, player2_word: str):
        valid1 = player1_word in MOVES
        valid2 = player2_word in MOVES

        if not valid1 and not valid2:
            return 0
        if not valid1:
            return 2
        if not valid2:
            return 1
        if player1_word == player2_word:
            return 0
        if BEATS[player1_word] == player2_word:
            return 1
        return 2
