import random


class game:
    def __init__(self):
        self.dice = [0, 0]
        self.board = [[1, 5], [0, 0], [0, 0], [0, 0], [2, 3], [0, 0], [2, 5], [0, 0], [0, 0], [0, 0], [0, 0], [1, 2],
                      [2, 2], [0, 0], [0, 0], [0, 0], [0, 0], [1, 5], [0, 0], [0, 0], [1, 3], [0, 0], [0, 0], [2, 5]]
        middle = [0, 0]

    def roll(self):
        self.dice [0] = random.randint(1, 6)
        self.dice [1] = random.randint(1, 6)

    def move(self, coordinate, move, other_player, player):
        if self.board [coordinate] [1] == player and self.board [coordinate + move] [0] != other_player:
            self.board [coordinate] [1] -= 1
            self.board [coordinate + move] [1] += 1
            if self.board [coordinate] [1] == 0:
                self.board [coordinate] [0] = 0
            self.board [coordinate + move] [0] = player
        elif self.board [coordinate] [0] == player and self.board [coordinate + move] [1] == 1:
            self.inMiddle(other_player)
            self.board [coordinate] [1] -= 1
            self.board [coordinate + move] [1] += 1
            if self.board [coordinate] [1] == 0:
                self.board [coordinate] [0] = 0

    def inMiddle(self, player):
        self.middle [player - 1] += 1

    def outMiddle(self, dice, player, other_player):
        i = 0
        while i != len(dice):
            if self.board [dice [i]] [0] != other_player and self.middle [player] > 0:
                choice = input("do you want to move your piece in the middle to space ", i,
                               " yes for yes, anything else will be interpreted as no.")
                if choice == "yes":
                    self.board [dice [i]] [0] = player
                    self.board [dice [i]] [1] += 1
                    self.middle [player] -= 1
                    del(dice[i])
                    i -= 1
            if self.board [dice [i]] [0] == other_player and self.board [dice [i]] [1] == 1:
                choice = input("do you want to move your piece in the middle to space ", i,
                               " yes for yes, anything else will be interpreted as no.")
                if choice == "yes":
                    self.board [dice [i]] [0] = player
                    self.board [dice [i]] [1] += 1
                    self.middle [player] -= 1
                    self.inMiddle(other_player)
                    del(dicce[i])
                    i -= 1
            i += 1
        if len(dice) > 0 :
            self.useRoll(dice, player, other_player)

    def isDouble(self, roll):
        try:
            del (roll [3])
            del (roll [2])
        except:
            pass
        if roll [0] == roll [1]:
            roll.append(roll [0])
            roll.append(roll [1])
        return (roll)

    def useRoll(self, roll, player, other_player):
        for i in range(len(roll) - 1):
            coordinate = -1
            while coordinate < 1 or coordinate > len(self.board):
                try:
                    coordinate = int(input("please enter the piece you want to move with your roll of ", roll [i]))
                except:
                    pass
            self.move(self, coordinate, roll [i], other_player, player)

    def turn(self, player, other_player):
        self.roll( )
        print("dice 1 : ", self.dice [0], "\n dice 2 : ", self.dice [1])
        if len(dice) == 4:
            print("dice 3 : ", self.dice [2], "\n dice 4 : ", self.dice [3])
        if self.middle [player - 1] != 0:
            self.outMiddle(dice, player)
        else:
            self.useRoll(dice, player, other_player)


game = game( )
for i in range(20):
    game.roll( )
    game.dice = game.isDouble(game.dice)
    print(game.dice)
