MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
}

def enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}")
            return False 
    return True 

def coins():
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction_complete(money_received,drink_cost):
    if money_received >= drink_cost:
        # rounding 2 decimal points
        change = round(money_received - drink_cost,2)
        print(f"Here  is {change} in change!")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Transaction failed! need ${drink_cost}. Money refunded")
        return False

def make_coffe(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

profit = 0
while True:
    user = input("What would you like? espresso/latte/cappuccino? \n").lower()
    if user == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: {profit}")
    elif user == "off":
        break
    else:
        drink = MENU[user]
        if enough(drink["ingredients"]):
            payment = coins()
            if transaction_complete(payment,drink['cost']):
                make_coffe(user,drink["ingredients"])
            