import art as ink
"""|This is a coffe machine that produces coffee
 , using dictionary as a unconventional database
 
 """



"""
using capital letters 'REPORT' variable(constant) 
so it can get through all the functions without calling it 
"""
REPORT = {
    "Water": 200,  # in ml
    "Milk": 500,  # in ml
    "Coffee": 100,  # in gram(g)
    # "Money": 500  # in dollar($)

}


def espresso():
    """
    checks for the availability of the ingredients available .
    and returns -1(dummy number to catch if the ingredients )
    :return -1:
    """

    # check_resourses = pass
    if REPORT["Water"] < 200 or REPORT["Coffee"] < 50:
        print("sorry, Not enough resources to produce espresso\nProvide enough resources to produce espresso")
        print(REPORT)
    else:

        return -1


def latte():
    """
    checks for the availability of the ingredients available .
    and returns -1(dummy number to catch if the ingredients )
    :return -1:
    """
    if REPORT["Water"] < 200 or REPORT["Coffee"] < 24 or REPORT["Milk"] < 150:
        print("sorry, Not enough resources to produce latte\nProvide enough resources to produce latte")
        print(REPORT)
    else:

        return -1


def cappuccino():
    """
    checks for the availability of the ingredients available .
    and returns -1(dummy number to catch if the ingredients )
    :return -1:
    """
    if REPORT["Water"] < 250 or REPORT["Coffee"] < 24 or REPORT["Milk"] < 100:
        print("sorry, Not enough resources to produce cappuccino\nProvide enough resources to produce cappucino")
        print(REPORT)
    else:

        return -1


def turnOff():
    # to turn of the machine

    print("Welcome to coffee maintainance\nHere are the list of ingredients")
    print(REPORT)
    ask = input("Type 'add' to add ingredients: ").lower()
    if ask == 'add':
        cof = int(input("How many ml if coffee do you want to add: "))
        REPORT["Coffee"] = REPORT["Coffee"] + cof

        water = int(input("How many ml if water do you want to add: "))
        REPORT["Water"] = REPORT["Water"] + water

        milk = int(input("How many ml if coffee do you want to add: "))
        REPORT["Milk"] = REPORT["Milk"] + milk
        print(REPORT)
        processCoins()



def checkingResources(rep):
    if rep["Money"] == 0:
        print("Not enough money ")
    else:
        pass





# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def askingMain():

    prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
    return prompt


def processCoins():
    """
    This is the main function where all other function run or are called
    it checks the askingmain input and validate the users money and also check the remaining ingredients
    :return:
    """

    asking_main = askingMain()
    if asking_main == "espresso":
        print("That would be $1.50")
        while True:
            ask_espresso = float(input("Enter your coin: "))
            if ask_espresso < 1.50:
                print(f"Your espresso cost $1.50 not ${ask_espresso}")
                continue
            else:
                ask_espresso -= 1.50
                coffee = espresso()
                if coffee == -1:
                    REPORT["Water"] = REPORT["Water"] - 50
                    REPORT["Coffee"] = REPORT["Coffee"] - 18
                    print(ink.log0)
                    print(f"Here's your  espresso ☕ and your  change of {ask_espresso}")
                    print(REPORT)
                    processCoins()

                else:
                    processCoins()
    elif asking_main == "latte":
        print("That would be $2.50")
        while True:
            ask_latte = float(input("Enter your coin: "))
            if ask_latte < 2.50:
                print(f"Your latte cost $2.50 not ${ask_latte}")
                continue
            else:
                ask_latte -= 2.50
                coffee = espresso()
                if coffee == -1:
                    REPORT["Water"] = REPORT["Water"] - 50
                    REPORT["Coffee"] = REPORT["Coffee"] - 18
                    REPORT["Milk"] = REPORT["Milk"] - 150
                    print(ink.log0)
                    print(f"Here's your Coffee Latte ☕ and your change of {ask_latte}")
                    print(REPORT)
                    processCoins()
                else:
                    processCoins()

    elif asking_main == "cappuccino":
        print("That would be $3.50")
        while True:
            ask_cappuccino = float(input("Enter your coin: "))
            if ask_cappuccino < 3.50:
                print(f"Your cappucino cost $3.50 not ${ask_cappuccino}")
                continue
            else:
                ask_cappuccino -= 3.50
                coffee = espresso()
                if coffee == -1:
                    REPORT["Water"] = REPORT["Water"] - 250
                    REPORT["Coffee"] = REPORT["Coffee"] - 24
                    REPORT["Milk"] = REPORT["Milk"] - 100
                    print(ink.log0)
                    print(f"Here's your Coffee cappucino ☕ and your  change of {ask_cappuccino}")
                    processCoins()
                else:
                    processCoins()
    elif asking_main == "off":
        turnOff()
    elif asking_main == "report":
        print(REPORT)

    else:
        print("invalid please")


print(ink.logo2)
processCoins()

