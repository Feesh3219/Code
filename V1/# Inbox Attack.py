# Inbox Attack V2

# Class parent class message
class Message:
    def __init__(self, sender, content, is_scam):
        self.sender = sender
        self.content = content
        self.is_scam = is_scam

    def display(self):
        print("----------------------------")
        print(f"From: {self.sender}")
        print(f"Message: {self.content}")
        print("----------------------------")

# Class scam message
# inherits from message - adds a warning
class ScamMessage(Message):
    def __init__(self, sender, content, warning):
        super().__init__(sender, content, is_scam=True)
        self.warning = warning

    def display(self):
        super().display()
        print(f"HINT: {self.warning}")

# Class SafeMessage
# inherits from message
class SafeMessage(Message):
    def __init__(self, sender, content):
        super().__init__(sender, content, is_scam=False)


# Player class to track score and name
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, points):
        self.score += points

    def show_score(self):
        print(f"Player: {self.name}")
        print(f"Score: {self.score}")    


# Game class to manage game flow
class Game:
    def __init__(self):
        self.player = None
        self.messages = []
    def setup(self):
        # Mix of scam and safe messages for the player
        self.messages.append(ScamMessage("Unknown Sender", "You've won a prize! Click here to claim.", "This is a common scam tactic."))
        self.messages.append(SafeMessage("Mum", "Hey are you coming home for dinner tonight???"))
        self.messages.append(ScamMessage("Nigerian Prince", "I need your help to transfer money. Please send your bank details.", "This is a classic scam however there is an extremely small chance of it being legitimate."))
        self.messages.append(SafeMessage("Mr skinner", "Don't forget to submit your software engineering assignment by April 23rd!"))
        # Maybe add one more message

    def ask_choice(self):
        # Keep asking until the player types a valid answer
        while True:
            choice = input("Do you want to open this message? (Open/Ignore): ").strip().lower()
            if choice in ['open', 'ignore']:
                return choice
            else:
                print("Invalid choice. Please type 'Open' or 'Ignore'.")

    def check_answer(self, message, choice):
        if message.is_scam and choice == 'Ignore':
            print("Correct! You avoided a scam.")
            self.player.update_score(10)
        elif not message.is_scam and choice == 'Open':
            print("Incorrect! That was a scam.")
            self.player.update_score(-10)
        elif not message.is_scam and choice == "open":
            print("Correct! That was a safe message.")
            self.player.update_score(10)
        else:
            # Add a message for ignoring a safe message later
            self.player.update_score(0)
        


    def start(self):
        print("Welcome to Inbox Attack!")
        self.setup()

        # Loop through messages
        for message in self.messages:
            print()
            message.display()
            choice = self.ask_choice()
            self.check_answer(message, choice)
            self.player.show_score()
            input("Press Enter to continue...")
        
        # End game
        print("Game Over!")
        self.player.show_score()
        # add final message based on players score

# Main
game = Game()
game.start()