# Inbox Attack

class Message:
    def __init__(self, sender, content, is_scam):
        self.sender = sender
        self.content = content
        self.is_scam = is_scam

def display(self):
    print(f"From: {self.sender}")
    print(f"Message: {self.content}")

class ScamMessage(Message):
    def __init__(self, sender, content, warning):
        super().__init__(sender, content, warning)
        self.warning = warning

    def display(self):
        super().display()
        pass
        # print self.warning later

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def update_score(self, points):
        pass
        # add points later
    def show_score(self):
        pass
        # display score later
    

class Game:
    def __init__(self):
        self.player = None
        self.messages = []
    def setup(self):
        pass
        # add asking for player naem and create object later
        # add scam and safemesage to self.messages later

    def ask_choice(self):
        pass
        # ask player to open or ignore later
        # return choice later

    def check_answer(self, message, choice):
        pass
        # if scam ignored add points later
        # if scam opened subtract points later
        # if safe opened add points later
        # if safe ignored no points later
    def start(self):
        print("welcome to Inmboxt attack")
        self.setup()
        # Loop through self.messages later
        # display each message
        # ask for achoice
        # check answer
        # show final score or smth

# Main
game = Game()
game.start()