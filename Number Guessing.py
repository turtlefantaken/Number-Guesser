#TODO: 1. Create a new public repository on GitHub.
#2. Complete the project according to the requirements and push your code to the GitHub repository.
#3. Add a README file with instructions to run the project and the project page URL
#4. Once done, submit your solution to help the others learn and get feedback from the community.

import random 
import time
def numberguess():
    secret_number = random.randint(1,100)

    #Easy Mode ()
    guess = int(input("Welcome to my Number Guessing game! Will you do Easy, Normal, or Hard mode?: \n 1.Easy (20 attempts) \n 2.Medium (10 attempts) \n 3.Hard (5 attempts): "))
    if guess == 1: #selecting the mode
        time.sleep(0.5)
        print("You picked Easy mode. Good luck!")
        attempts = 0
        max_attempts = 20 
        while attempts != max_attempts: 
            try:  #tells the user if the number they picked is bigger or smaller than the actual number
                guess = int(input("Pick a number from 1 to 100: "))
                attempts += 1
                if guess < secret_number: 
                    print(f"The number is bigger than {guess}")
                if guess > secret_number:
                    print(f"The number is smaller than {guess}")
                if guess == secret_number:
                    print("You did it! Good job! Thank you very much for playing.")
            finally: 
                if attempts == max_attempts: #if they mess up too many times
                    print(f"Sorry, you didn't get it. The number was {secret_number}.")
                    time.sleep(1)
                    break

    #Medium Mode
    if guess == 2: 
        time.sleep(0.5)
        print("You picked Medium mode. Good luck!")
        attempts = 0 
        max_attempts = 10
        while attempts != max_attempts:
            try:
                guess = int(input("Pick a number from 1 to 100: "))
                attempts += 1
                if guess < secret_number: 
                    print(f"The number is bigger than {guess}")
                if guess > secret_number:
                    print(f"The number is smaller than {guess}")
                if guess == secret_number:
                    print("You did it! Good job! Thank you very much for playing.")
            finally: 
                if attempts == max_attempts:
                    print(f"Sorry, you didn't get it. The number was {secret_number}.")
                    time.sleep(1)
                    break
    
    #Hard Mode
    if guess == 3: 
        time.sleep(0.5)
        print("You picked Hard mode. Good luck!")
        attempts = 0 
        max_attempts = 5
        while attempts != max_attempts:
            try:
                guess = int(input("Pick a number from 1 to 100: "))
                attempts += 1
                if guess < secret_number: 
                    print(f"The number is bigger than {guess}")
                if guess > secret_number:
                    print(f"The number is smaller than {guess}")
                if guess == secret_number:
                    print("You did it! Good job! Thank you very much for playing.")
            finally: 
                if attempts == max_attempts:
                    print(f"Sorry, you didn't get it. The number was {secret_number}.")
                    time.sleep(1)
                    break



                        
            

numberguess()