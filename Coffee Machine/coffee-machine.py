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

register_money = 0

def payment_method(menu_dict, user_key):
    price = menu_dict[user_key]["cost"]
    
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01
    
    print("Please insert coins.")
    
    user_quarters = int(input("how many quarters?: "))
    user_dimes = int(input("how many dimes?: ")) 
    user_nickels = int(input("how many nickels?: ")) 
    user_pennies = int(input("how many pennies?: "))
    
    total_paid = (user_quarters * quarters) + (user_dimes * dimes) + (user_nickels * nickels) + (user_pennies * pennies)
    user_change = round(total_paid - price, 2)
    
    if total_paid >= price:
        global register_money
        register_money += price
        if user_change > 0:
            print(f"Here is ${user_change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def brew_coffee(coffee_name, other_ingredients):
    for item in other_ingredients:
        resources[item] -= other_ingredients[item]
    print(f"Here is your {coffee_name} ☕. Enjoy!")

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${register_money}")
    
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

is_ordering = True

while is_ordering:
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    
    if user_order in ["espresso", "latte", "cappuccino"]:
        coffee = MENU[user_order]
        if is_resource_sufficient(coffee["ingredients"]):
            if payment_method(MENU, user_order):
                brew_coffee(user_order, coffee["ingredients"])
    
    elif user_order == "report":
        report()
    
    elif user_order == "off":
        is_ordering = False
        print("We've closed for the day, see you next time.")
