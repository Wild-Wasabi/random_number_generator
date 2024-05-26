import random

user_preference = ""
iterationCount = 0
operatorQuestioning = True
user_input = input("Number of times code will run: ")

while (not user_input.isnumeric()):
    user_input = input("Type a positive number: ")
#test
# while (user_input.lower() != "quit"):
#Runs this many times if quit not typed
for x in range(0, int(user_input)):

    #Always runs first time, if user doesn't want to change, skips
    if (iterationCount < 1 or operatorQuestioning):
        #Asks for operator
        user_preference = input("Which operator would you like to use?\na   s   m   d   Any:\n")

        while (user_preference.lower() != "a" and user_preference.lower() != "s" and user_preference.lower() != "m" and user_preference.lower() != "d" and user_preference.lower() != "any"):
            user_preference = input("Please enter one of these.\na   s   m   d   Any:\n")

    #Asks if user wants to change operator
    if (iterationCount < 1):
        user_input = input("You would like to change the operator?\nTrue   False\n")
        while (user_input.lower() != "true" and user_input.lower() != "false"):
            user_input = input("True or False: ")
        if(user_input.lower() == "false"):
            operatorQuestioning = False

    print("Type quit to leave")

    #User number for equation to equate to
    user_input = input("Type a positive number: ")

    while (not user_input.isnumeric()):

        if(user_input.lower() == "quit"):
            break
    
        user_input = input("Type a POSITIVE NUMBER: ")

    if(user_input.lower() == "quit"):
            break   

    #Randomly generates operator
    random_num = random.randint(0, 99)

    #Chooses pre-selected operator
    if(user_preference == "a"):
        random_num = 0
    if(user_preference == "s"):
        random_num = 25
    if(user_preference == "m"):
        random_num = 50
    if(user_preference == "d"):
        random_num = 75

    user_num = int(user_input)
    super_random_number = random.randint(1, 10000)

    #add
    if (random_num < 25):
        additive_2 = user_num - super_random_number
        print(super_random_number, "+", additive_2, "=", user_num)
    #subtract
    elif (random_num < 50):
        difference = super_random_number - user_num
        print(super_random_number, "-", difference, "=", user_num)
    #multiply
    elif (random_num < 75):
        multiplier_2 = user_num / super_random_number
        print(super_random_number, "*", multiplier_2, "=", user_num)
    #divide
    elif (random_num < 100):
        total = user_num * super_random_number
        print(total, "/", super_random_number, "=", user_num)

    iterationCount += 1