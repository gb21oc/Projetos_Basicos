import win32api
from random import randint


class MiniGame:
    user_name = win32api.GetUserName()
    options = ["Stone", "Paper", "Scissors"]
    punctuation_user = 0
    punctuation_bot = 0
    sum_punctuation = 0

    def resetting_score(self):
        self.punctuation_user = 0
        self.punctuation_bot = 0
        self.sum_punctuation = 0

    @classmethod
    def validate_info_user(cls, userChoice):
        try:
            # num_str = str(userChoice)
            if userChoice == "" or userChoice is None:
                print("\n[-] Please type something so we can play! :) \n")
                return True
            if not userChoice.isnumeric():
                print("\n[-] Please type only number!!! :/ \n")
                return True
            if int(userChoice) > 2:
                print("\n[-] Please choose from 0 to 2!!!!\n")
                return True
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
            self.punctuation_user += 1
            return
        if self.options[choose_user] == "Paper" and self.options[choose_bot] == "Stone":
            print(f"[+] Congratulations {self.user_name} you won!!!! +1 Score!!!")
            self.punctuation_user += 1
            return
        if self.options[choose_user] == "Scissors" and self.options[choose_bot] == "Paper":
            print(f"[+] Congratulations {self.user_name} you won!!!! +1 Score!!!")
            self.punctuation_user += 1
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
            you_continue = True
            print(f"[+] Hi! How are you? Let's start our game {self.user_name}?\n")
            while you_continue:
                print(f"[+] Chooses one of the options below: ")
                print(f"    => [0] for Stone(Pedra)")
                print(f"    => [1] for Paper(Papel)")
                print(f"    => [2] for Scissors(Tesoura)")

                if self.punctuation_user > 0 or self.punctuation_bot > 0:
                    print(f"\n[+] Your punctuation: {self.punctuation_user}")
                    print(f"[+] BOT punctuation: {self.punctuation_bot}")

                userChoice = input("[+] What will be your choice? ")
                if self.validate_info_user(userChoice):
                    continue
                print("[+] Thinking....\n")
                choose_bot = self.robot_choice()
                self.result_of_choices(choose_bot, int(userChoice))
                self.sum_punctuation = self.punctuation_user + self.punctuation_bot

                if self.sum_punctuation == 3 or self.punctuation_user == 3 or self.punctuation_bot == 3:
                    if self.punctuation_user > self.punctuation_bot:
                        print(f"[+] Your punctuation: {self.punctuation_user}")
                        print(f"[-] BOT punctuation: {self.punctuation_bot}")
                        print("     [+] You won me !!! next time i will be the winner :c")
                    else:
                        print(f"[+] Your punctuation: {self.punctuation_user}")
                        print(f"[+] BOT punctuation: {self.punctuation_bot}")
                        print(f"     [-] Hahaha I won, if you wanted to beat me you'll have to make an effort! Loser "
                              f"{self.user_name}")

                    result_continue = input("[+] Do you wish to continue? [Y(yes) / N(No)]")
                    if result_continue.upper() == "Y":
                        self.resetting_score()
                        you_continue = True
                    elif result_continue.upper() == "N":
                        print("\n[+] It was good to play with you, see you later!")
                        self.resetting_score()
                        you_continue = False
                    else:
                        print("[-] Please choose between Y or N.")
                        return

        except (IndexError, Exception, BaseException, ValueError):
            print("[-] An unexpected error has occurred! :/ ")


if __name__ == "__main__":
    MiniGame().main()

"""
-> Verifica se o numero é repetido
# if len(str(userChoice)) >= 1 and (len(str(userChoice)) * num_str[0]) == userChoice:
#     print("\n[-] Please choose from 0 to 2!!!!\n")
#     return True
"""