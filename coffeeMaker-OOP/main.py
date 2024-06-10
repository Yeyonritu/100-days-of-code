from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_ordering = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_ordering = True

while is_ordering:
    
    user_order = input(f"What would you like? ({menu.get_items()}): ")
    
    if user_order == "off":
        is_ordering = False
        print("We are now closed. See you later!")
        
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()
        
    else:
            
        drink = menu.find_drink(user_order)
        drink_cost = drink.cost
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink_cost) :
            coffee_maker.make_coffee(drink)
            
    
    
    
    