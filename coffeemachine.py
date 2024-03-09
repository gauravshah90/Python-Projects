import clear

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit":0
}


# TODO 2: Check Resources are sufficient
def check_resources(coffee_name):
    if MENU[user_input]["ingredients"]["water"]<resources["water"] and MENU[user_input]["ingredients"]["coffee"]<resources["coffee"] and MENU[user_input]["ingredients"]["milk"]<resources["milk"]:
        return (True)
    else:
        print("Sorry! Machine is low on resources")
        return (False)

def process_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_collection = quarters*0.25 + dimes*0.10 + nickles*0.05+ pennies*0.01
    if total_collection >= MENU[user_input]["cost"]:
        return_amount = round(total_collection - MENU[user_input]["cost"],2)
        print(f"here is your change {return_amount}")
        return (True)
    else:
        print(f"Sorry insufficient amount. Collect your ${total_collection}")
        return(False)

def make_coffee(user_input):
    resources["water"] -= MENU[user_input]["ingredients"]["water"]
    resources["coffee"] -=MENU[user_input]["ingredients"]["coffee"]
    resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
    resources["profit"] += MENU[user_input]["cost"]
    print(f"your coffee: {user_input} is ready!")

machine_status = True
while machine_status == True:
    coffee_status = True
    while coffee_status == True:
        user_input = input("What would you like? (espresso/latte/cappuccino):\n")
        if user_input =='off':
            machine_status = False
            coffee_status = False
        elif user_input == 'report':
            print(f"water = {resources["water"]}ml")
            print(f"milk = {resources["milk"]}ml")
            print(f"coffee = {resources["coffee"]}g")
            print(f"profit = ${resources["profit"]}")
            coffee_status = False
        else:
            coffee_status = check_resources(user_input)
            if coffee_status == True:
                coffee_status = process_coins()
                if coffee_status == True:
                    make_coffee(user_input)



# TODO 1: Print Report

# TODO 3: Process Coins
# TODO 4: Check Transaction Successful
# TODO 5: Make Coffee
