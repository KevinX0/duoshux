#Duoshu Xu (collabrates with Manhua Chen)

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

# - Play once and report the result
def who_is_winner(p1, p2):
    if p1 == p2:
        return 'tie'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'win'
    else:
        return 'lose'

result = who_is_winner(p1, p2)
print(f'Player 2 chose: {p2}')
print(f'You {result}!')

# - Play in a loop and record how many wins and losses happen?
def who_is_winner(p1, p2):
    if p1 == p2:
        return 'tie'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'win'
    else:
        return 'lose'
    
wins = 0
losses = 0
ties = 0

for _ in range(3):  
    p1 = input('Pick one of rock, paper or scissors: ')
    p2 = random.choice(choices)
    result = who_is_winner(p1, p2)
    print(f'Player 2 chose: {p2}')
    if result == 'win':
        wins += 1
    elif result == 'lose':
        losses += 1
    else:
        ties += 1
    print(f'You {result}!')

print(f'Total Results: {wins} wins, {losses} losses, and {ties} ties.')

# - Organize everything into classes??
class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def get_player1_choice(self):
        choice = input('Pick one of rock, paper or scissors: ')
        while choice not in self.choices:
            print("Invalid input. Please choose from rock, paper, or scissors.")
            choice = input('Pick one of rock, paper or scissors: ')
        return choice

    def get_player2_choice(self):
        return random.choice(self.choices)

    def who_is_winner(self, p1, p2):
        if p1 == p2:
            return 'tie'
        elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
            return 'win'
        else:
            return 'lose'

    def play_round(self):
        p1 = self.get_player1_choice()
        p2 = self.get_player2_choice()
        result = self.who_is_winner(p1, p2)
        print(f'Player 2 chose: {p2}')
        print(f'You {result}!')
        return result

    def play_game(self, num_rounds):
        for _ in range(num_rounds):
            result = self.play_round()
            if result == 'win':
                self.wins += 1
            elif result == 'lose':
                self.losses += 1
            else:
                self.ties += 1

        print(f'Total results: {self.wins} Wins, {self.losses} Losses, {self.ties} Ties.')
game = RockPaperScissors()
game.play_game(5) 

