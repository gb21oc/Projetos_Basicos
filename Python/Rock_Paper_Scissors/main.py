import win32api
from random import randint


class MiniGame:
    user_name = win32api.GetUserName()
    options = ["Stone", "Paper", "Scissors"]
    punctuation_user = 0
    punctuation_bot = 0

    @classmethod
    def validate_info_user(cls, userChoice):
        try:
            if userChoice == "" or userChoice is None:
                print("[-] Please type something so we can play! :) ")
            if not userChoice.isnumeric():
                print("[-] Please type only number!!! :/ ")
            # if userChoice != 0 or userChoice != 1 or userChoice != 2:
                #print("[-] Please choose only of the options above! :/ ")
        except (IndexError, Exception, BaseException, ValueError):
            print("[-] An unexpected error has occurred! :/ ")

    @classmethod
    def robot_choice(cls):
        try:
            number_choose = randint(0, 2)
            return number_choose
        except (IndexError, Exception, BaseException, ValueError):
            print("[-] An unexpected error has occurred! :/ ")

    def result_of_choices(self, choose_bot, choose_user):
        # Draw
        if choose_user == choose_bot:
            print("[+] It was a tie :), let's try again")
            return

        # User
        if self.options[choose_user] == "Stone" and self.options[choose_bot] == "Scissors":
            print(f"[+] Congratulations {self.user_name} you won!!!! +1 Score!!!")
            MiniGame.punctuation_user += 1
            return
        if self.options[choose_user] == "Paper" and self.options[choose_bot] == "Stone":
            print(f"[+] Congratulations {self.user_name} you won!!!! +1 Score!!!")
            MiniGame.punctuation_user += 1
            return
        if self.options[choose_user] == "Scissors" and self.options[choose_bot] == "Paper":
            print(f"[+] Congratulations {self.user_name} you won!!!! +1 Score!!!")
            MiniGame.punctuation_user += 1
            return

        # Bot
        if self.options[choose_bot] == "Stone" and self.options[choose_user] == "Scissors":
            print(f"[+] Congratulations bot_ you won!!!! +1 Score!!!")
            MiniGame.punctuation_bot += 1
            return
        if self.options[choose_bot] == "Paper" and self.options[choose_user] == "Stone":
            print(f"[+] Congratulations bot_ you won!!!! +1 Score!!!")
            MiniGame.punctuation_bot += 1
            return
        if self.options[choose_bot] == "Scissors" and self.options[choose_user] == "Paper":
            print(f"[+] Congratulations bot_ you won!!!! +1 Score!!!")
            MiniGame.punctuation_bot += 1
            return

    def main(self):
        try:
            print(self.punctuation_user)
            you_continue = True
            print(f"[+] Hi! How are you?")
            print(f"[+] Let's start our game {self.user_name}?")
            while you_continue:
                print(f"[+] Chooses one of the options below: ")
                print(f"    => [0] for Stone(Pedra)")
                print(f"    => [1] for Paper(Papel)")
                print(f"    => [2] for Scissors(Tesoura)")
                userChoice = input("[+] What will be your choice? ")
                print("[+] Thinking....")
                MiniGame.validate_info_user(userChoice)
                choose_bot = MiniGame().robot_choice()
                MiniGame().result_of_choices(choose_bot, int(userChoice))
                result_continue = input("[+] Do you wish to continue? [Y(yes) / N(No)]")
                if result_continue.upper() == "Y":
                    print("[+] Alright let's continue!!! ")
                    if self.punctuation_user > self.punctuation_bot:
                        print("     [+] You are winning me!!! But i will turn this game around :) ")
                    elif self.punctuation_user == self.punctuation_bot:
                        print("     [+] We are tied!!")
                    else:
                        print(f"    [+] Hahaha I'm winning, if you wanted to win me you'll have to make an affort! Loser {self.user_name} ")
                    you_continue = True
                elif result_continue.upper() == "N":
                    print("     [+] It was good to play with you, the score was like this: ")
                    print(f"        {self.user_name}: {self.punctuation_user}")
                    print(f"        bot_: {self.punctuation_bot}")
                    you_continue = False
                else:
                    print("[-] Please choose between Y or N.")


        except (IndexError, Exception, BaseException, ValueError) as err:
            print("[-] An unexpected error has occurred! :/ " + str(err))


if __name__ == "__main__":
    MiniGame().main()
