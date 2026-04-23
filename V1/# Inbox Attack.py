
# Inbox Attack V3

# class parent class message
# Stores basic details of a message - sender, content, and whether it's a scam or not
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


# ScamMessage inherits from Message - adds a warning
# explanation is for the reason its a scam
class ScamMessage(Message):
    def __init__(self, sender, content, warning, explanation):
        super().__init__(sender, content, is_scam=True)
        self.warning = warning
        self.explanation = explanation

    def display(self):
        super().display()
        print(f"HINT: {self.warning}")


# SafeMessage inherits from Message
# Explanation is for the reason its safe
class SafeMessage(Message):
    def __init__(self, sender, content, explanation):
        super().__init__(sender, content, is_scam=False)
        self.explanation = explanation


# Player class to track name and score
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, points):
        self.score += points

    def show_score(self):
        print(f"Player: {self.name}")
        print(f"Score: {self.score} points")

    def get_result(self):
        if self.score >= 30:
            return "Cyber security Expert! You spotted every scam."
        elif self.score >= 10:
            return "Not bad! You caught most scams but missed a few."
        else:
            return "Your kinda buns. Be more careful."


# Game class to manage game flow
class Game:
    def __init__(self):
        self.player = None
        self.messages = []

    def setup(self):
        # Ask for player name and create Player object
        name = input("Enter your name: ").strip()
        if name == "":
            name = "Player"
        self.player = Player(name)

        # Mix of scam and safe messages for the player
        self.messages.append(ScamMessage(sender="Unknown Sender", content="You've won a prize! Click here to claim.", warning="This is a common scam tactic.", explanation="Scammers use fake prizes to get you to click malicious links."))
        self.messages.append(SafeMessage(sender="Mum", content="Hey are you coming home for dinner tonight???", explanation="This is a SAFE message! Known contact, no suspicious links or requests."))
        self.messages.append(ScamMessage(sender="Nigerian Prince", content="I need your help to transfer money. Please send your bank details.", warning="Never send your bank details to anyone online.",explanation="This is one of the oldest scams around. No real prince needs your bank details or your money."))
        self.messages.append(SafeMessage(sender="Mr Skinner", content="Don't forget to submit your software engineering assignment by April 23rd!", explanation="Totally safe. Known sender with a normal school request."))


    def ask_choice(self):
        # Keep asking until the player types a valid answer
        while True:
            choice = input("Do you want to open this message? (open / ignore): ").strip().lower()
            if choice in ['open', 'ignore']:
                return choice
            else:
                print("Invalid choice. Please type 'open' or 'ignore'.")

    def check_answer(self, message, choice):
        # Selection - work out outcome based on choice and message type
        if message.is_scam and choice == 'ignore':
            print("Correct! You avoided a scam. +10 points")
            self.player.update_score(10)
        elif message.is_scam and choice == 'open':
            print("You fell for it! That was a scam. -5 points")
            self.player.update_score(-5)
        elif not message.is_scam and choice == 'open':
            print("Correct! That was a safe message. +10 points")
            self.player.update_score(10)
        else:
            print("That was a safe message, but no harm done. 0 points")
            self.player.update_score(0)

        # explanation after the choice
        print(f"LEARN: {message.explanation}")

    def start(self):
        print("INBOX ATTACK")
        print("Read each message and decide whether to open or ignore it.")
        print("Ignore scams. Open safe messages.")

        self.setup()

        # Loop through every message one by one
        for i, message in enumerate(self.messages, 1):
            print(f"Message {i} of {len(self.messages)}")
            message.display()
            choice = self.ask_choice()
            self.check_answer(message, choice)
            print()
            self.player.show_score()
            input("Press Enter to continue")

        # Final screen
        print("--------------------------------")
        print("         GAME OVER")
        print("--------------------------------")
        self.player.show_score()
        print(f"Result: {self.player.get_result()}")
        print("Key cyber safety tips:")
        print("- Never click links in unexpected messages")
        print("- If you do not know, ignore and ask a trusted adult")


# Main
game = Game()
game.start()
