shopping_list = []

# Some common grocery items you can pick from
available_items = [
    "Milk",
    "Bread",
    "Eggs",
    "Butter",
    "Cheese",
    "Apples",
    "Bananas",
    "Rice",
    "Chicken",
    "Tomatoes"
]

def show_menu():
    
    print("Welcome to your Shopping List Manager!")
    print("Here's what you can do:")
    print("1. See what's on your shopping list")
    print("2. Add something from our grocery list")
    print("3. Remove something from your shopping list")
    print("4. Start fresh by clearing your shopping list")
    print("5. Take a look at all the grocery items you can add")
    print("6. Exit the program (we'll miss you!)")

def show_shopping_list():
    if not shopping_list:
        print("Looks like your shopping list is empty right now.")
    else:
        print("Here's your current shopping list:")
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")

def show_available_items():
    print("Here are the items you can add:")
    for idx, item in enumerate(available_items, 1):
        print(f"{idx}. {item}")

def add_item():
    show_available_items()
    try:
        choice = int(input("Choose the item number you'd like to add: "))
        if 1 <= choice <= len(available_items):
            item = available_items[choice - 1]
            shopping_list.append(item)
            print(f"Added '{item}' to your shopping list. Nice choice!")
        else:
            print("Hmm, that number doesn't match any item. Try again?")
    except ValueError:
        print("Oops! Please type a valid number.")

def remove_item():
    show_shopping_list()
    if shopping_list:
        try:
            index = int(input("Enter the number of the item you want to remove: "))
            if 1 <= index <= len(shopping_list):
                removed = shopping_list.pop(index - 1)
                print(f"Removed '{removed}' from your list. Got it!")
            else:
                print("That number isn't in your shopping list. Double-check?")
        except ValueError:
            print("Please enter a number, not letters or symbols.")

def clear_list():
    shopping_list.clear()
    print("Your shopping list is now empty. Fresh start!")

while True:
    show_menu()
    choice = input("What would you like to do? (Enter a number 1-6): ").strip()

    if choice == '1':
        show_shopping_list()
    elif choice == '2':
        add_item()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        clear_list()
    elif choice == '5':
        show_available_items()
    elif choice == '6':
        print("Thanks for stopping by! Happy shopping!")
        break
    else:
        print("Oops, that choice doesn't look right. Please pick a number between 1 and 6.")
