import sys
import os

cookbook = {
        'sandwich': {
            'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
            'meal': 'lunch',
            'prep_time': 10
            },
        'cake': {
            'ingredients': ['flour', 'sugar', 'eggs'],
            'meal': 'dessert',
            'prep_time': 60
            },
        'salad': {
            'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
            'meal': 'lunch',
            'prep_time': 15
            }
        }
def print_recipe(name):
    if name in cookbook:
        print(f"\nRecipe for {name}:\n"
                f"Ingredients list: {cookbook[name]['ingredients']}\n" +
                f"To be eaten for {cookbook[name]['meal']}.\n" +
                f"Takes {cookbook[name]['prep_time']} minutes of cooking.\n")
    else:
        print("That recipe is not in the cookbook!\n")

def del_recipe(name):
    if name in cookbook:
        del cookbook[name]
        print(f"Recipe {name} has been deleted\n")
    else:
        print("That recipe is not in the cookbook!\n")

def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
            'ingredients': ingredients.split(','),
            'meal': meal,
            'prep_time': prep_time
            }
    print(f"Recipe {name} has been added to the cookbook\n")

def print_all_recipes():
    if len(cookbook) == 0:
        print("There are no recipes to print!\n")
    else:
        for name in cookbook:
            print_recipe(name)

def interact():
    num = int(input("""Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit\n"""))
    if num < 1 or num > 5:
        print("This option does not exist, please type the corresponding"
                " number\n")
    else:
        return num


def main():
    try:
        num = interact()
        if num == 1:
            name = input("What is the recipe name that you want to add?\n")
            if not(name):
                print("The recipe has to have a name!")
            else:
                ingredients = input("What are its ingredients?\n")
            if not(ingredients):
                print(f"{name} has to have ingredients!")
            else:
                meal = input("What is the optimal eating time?\n")
            if not(meal):
                print(f"Tell me when is the best time to eat {name}!")
            else:
                prep_time = input("How long does it take to prepare?\n")
            if not(prep_time.isdecimal()):
                print(f"I need to know how many minutes it takes to prepare"
                " {name}!")
            else:
                add_recipe(name, ingredients, meal, prep_time)
        elif num == 2:
            name = input("What is the name of the recipe that you wish to"
                    " delete?\n")
            del_recipe(name)
        elif num == 3:
            name = input("What recipe would you like to see?\n")
            print_recipe(name)
        elif num == 4:
            print_all_recipes()
        elif num == 5:
            print("Ok Bye!")
            exit()
        main()
    except KeyboardInterrupt:
        print("Ok bye!")
    except ValueError:
        main()

main()
