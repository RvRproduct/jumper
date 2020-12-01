import random
import sys
import string


class Jumper:
    def __init__(self):
        self.chute =  []
        self.chute.append(r"  ___  ")
        self.chute.append(r" /___\ ")
        self.chute.append(r" \   / ")
        self.chute.append(r"  \ /  ")
        self.chute.append(r"   0   ")
        self.chute.append(r"  /|\  ")
        self.chute.append(r"  / \  ")
        self.chute.append(r"       ")
        self.chute.append(r"^^^^^^^")

    def cut_line(self):
        del self.chute[0]


    def is_alive(self):
        is_alive = True
        if len(self.chute) <= 4:
            self.chute.insert(0,(r"   X   "))
            is_alive = False
        return is_alive

    
    def get_chute(self, choice):
        self.objective = []
        self.objective.clear()
        symbol = ""

        if choice.lower() == "solo":
            for letter in range(5):
                self.objective.append(random.choice(string.ascii_letters))
        elif choice.lower() == "multi":
            counter = 5
            for letter in range(5):
                symbol = ""
                while len(symbol) != 1:
                    symbol = input(f"Choose a letter {counter} left: \n")
                counter -= 1
                self.objective.append(symbol)
        return (self.objective)

            

class Target(Jumper):
    def __init__(self):
        self.guesses = ["_", "_", "_", "_", "_"]
        self.guessed_bad = []
        self.guess = ""
        self.right = False
        choice = ""
        while choice.lower() not in("solo", "multi"):
            choice = input("\nWould you like to play with friends or alone {solo, multi): ")
        self.letters = super().get_chute(choice)

    
    def has_letter(self, guess):
        for index, letter in enumerate(self.letters):
            if guess == letter:
                self.guesses[index] = guess
                self.right = True
        if guess not in(self.letters):
            self.guessed_bad.append(guess)
            self.right = False

    
    def is_found(self):
        if  self.guesses == self.letters:
            return True
        else:
            return False

    def get_guesses(self):
        self.guess = ""
        while len(self.guess) != 1 and len(self.guess) > 1: 
            self.guess = input("Guess a letter: ")
        return self.guess


class Trainer:
    def start_jump(self):
        jumper = Jumper()
        target = Target()

        while jumper.is_alive() and not target.is_found():
            target.get_guesses()
            guess = target.guess
            target.has_letter(guess)
            if not target.right:
                jumper.cut_line()
                print(target.guesses)
                print(target.guessed_bad)
        
                for x in jumper.chute:
                    print(x)
               
               

if __name__ == "__main__":
    trainer = Trainer()
    trainer.start_jump()