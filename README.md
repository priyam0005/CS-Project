# Shopping List Manager - README

## Project Overview

The Shopping List Manager is a Python-based menu-driven application designed to help users manage their shopping lists efficiently. This project demonstrates core Python programming concepts including functions, loops, conditional statements, and list manipulation. The application allows users to add, view, remove, and clear items from their shopping list with a user-friendly interface.

---

## Features

- **View Shopping List**: Display all items currently on your shopping list
- **Add Items**: Select items from a predefined list of grocery items to add to your shopping list
- **Remove Items**: Delete specific items from your shopping list by selecting their number
- **Clear List**: Remove all items at once to start fresh
- **View Available Items**: Browse the complete list of items you can add
- **User-Friendly Interface**: Conversational prompts and error handling for a smooth experience

---

## Technical Details

### Technologies Used
- **Language**: Python 3.x
- **Concepts**: Functions, Loops, Lists, Conditionals, User Input Handling
- **No External Dependencies**: Pure Python - no libraries or datasets required

### System Requirements
- Python 3.x installed on your system
- Any text editor or IDE (VS Code, PyCharm, IDLE, etc.)
- Terminal or command prompt access

---

## Installation and Running

### Steps to Run:

1. **Save the Code**: Copy the provided Python code and save it as `shopping_list_manager.py`

2. **Open Terminal/Command Prompt**: Navigate to the directory where you saved the file

3. **Run the Program**:
   ```
   python shopping_list_manager.py
   ```

4. **Interact with the Menu**: Follow the on-screen prompts to manage your shopping list

---

## User Guide

### Main Menu Options

| Option | Function | Description |
|--------|----------|-------------|
| 1 | View Shopping List | Displays all items you've added to your shopping list |
| 2 | Add Item | Shows available grocery items to choose from and adds selected item to your list |
| 3 | Remove Item | Removes a specific item from your shopping list by its number |
| 4 | Clear List | Removes all items from your shopping list at once |
| 5 | View Available Items | Shows all grocery items available for selection |
| 6 | Exit | Closes the program |

### Step-by-Step Usage Example

**Example Scenario: Adding items to your shopping list**

1. Run the program
2. Choose option `2` (Add Item from Available Items)
3. View the list of available items (numbered 1-10)
4. Enter the item number you want to add (e.g., `3` for Eggs)
5. The item is added with a confirmation message
6. Return to main menu and repeat as needed

**Example Scenario: Removing items**

1. Choose option `3` (Remove Item)
2. Your current shopping list is displayed
3. Enter the number of the item you want to remove
4. Item is removed with confirmation
5. Your updated list is displayed

---

## Code Structure Explanation

### Main Components

**1. Data Structure**
```
shopping_list = []  # Stores user's selected items
available_items = []  # Predefined list of grocery items
```

**2. Key Functions**

- `show_menu()`: Displays main menu options
- `show_shopping_list()`: Displays current items in the shopping list
- `show_available_items()`: Shows all available items to select from
- `add_item()`: Adds selected item to shopping list
- `remove_item()`: Removes item from shopping list
- `clear_list()`: Empties the entire shopping list

**3. Main Loop**
```
while True:
    # Display menu
    # Get user choice
    # Execute corresponding function
    # Continue until user exits
```

---

## Hardcoded Available Items

The application comes with a predefined list of 10 common grocery items:

1. Milk
2. Bread
3. Eggs
4. Butter
5. Cheese
6. Apples
7. Bananas
8. Rice
9. Chicken
10. Tomatoes

These items can be easily modified in the code by editing the `available_items` list.

---

## Error Handling

The program includes robust error handling:

- **Invalid Number Input**: If user enters non-numeric input when selecting an item
- **Out of Range Selection**: If user enters a number outside available options
- **Empty List Operations**: Handles attempts to remove items from an empty list
- **Input Validation**: Strips whitespace and validates all user inputs

### Error Messages

- "Oops! Please type a valid number." - When non-numeric input is provided
- "Hmm, that number doesn't match any item. Try again?" - When number is out of range
- "That number isn't in your shopping list. Double-check?" - When trying to remove non-existent item

---

## Limitations

1. **No Data Persistence**: All data is lost when the program exits (not saved to file)
2. **Single Item Addition**: Can only add one item at a time
3. **No Quantity Tracking**: Doesn't track how many of each item to buy
4. **Fixed Item List**: Limited to predefined grocery items only
5. **No Category Filtering**: Items are not organized by category
6. **No Priority System**: Cannot mark items as urgent or important

---

## Future Enhancement Ideas

1. **File Saving**: Save shopping list to a text file and load previous lists
2. **Quantity Tracking**: Add quantity field for each item (e.g., 2 Milk, 1 Bread)
3. **Price Tracking**: Include item prices and calculate total cost
4. **Custom Items**: Allow users to add items not in the predefined list
5. **Item Categories**: Organize items by category (Dairy, Vegetables, Grains, etc.)
6. **Priority Levels**: Mark items as high/medium/low priority
7. **Search Function**: Search for specific items in the list
8. **Multiple Lists**: Create and manage multiple shopping lists
9. **Database Integration**: Use SQLite to persist data
10. **GUI Interface**: Convert to graphical interface using tkinter or PyQt

---

## Learning Outcomes

By building this project, you will learn:

### Python Fundamentals
- Function definition and calling
- Parameter passing and return values
- While loops for continuous menu display
- For loops for iterating through lists

### Data Structure Management
- List operations (append, pop, clear, enumerate)
- Indexing and slicing
- Dynamic data manipulation

### User Interaction
- Input validation and error handling
- Exception handling with try-except blocks
- User-friendly output formatting

### Programming Practices
- Code organization with functions
- DRY (Don't Repeat Yourself) principle
- Meaningful variable names
- Comments and documentation

---

## Example Code Walkthrough

```python
# When user chooses option 2 (Add Item):
def add_item():
    show_available_items()  # Display available choices
    try:
        choice = int(input("Choose the item number you'd like to add: "))
        # Try to convert input to integer
        
        if 1 <= choice <= len(available_items):
            # Check if choice is valid
            item = available_items[choice - 1]
            # Get item at chosen index (subtract 1 for 0-based indexing)
            
            shopping_list.append(item)
            # Add item to shopping list
            
            print(f"Added '{item}' to your shopping list. Nice choice!")
    except ValueError:
        print("Oops! Please type a valid number.")
```

---

## Troubleshooting

**Issue**: Program doesn't run
- **Solution**: Ensure Python 3.x is installed. Run `python --version` to check.

**Issue**: Menu options not working
- **Solution**: Ensure you're entering numbers 1-6, not letters or special characters.

**Issue**: Can't add items
- **Solution**: Check that you're selecting a number that corresponds to an available item.

**Issue**: Program crashes when removing items
- **Solution**: Make sure your shopping list is not empty before attempting to remove items.

---

## How to Modify the Code

### Adding More Items to the List
```python
available_items = [
    "Milk",
    "Bread",
    # ... existing items
    "Your New Item Here"
]
```

### Changing Menu Messages
Simply edit the strings in the `show_menu()` function to customize messages.

### Adding New Features
Follow the existing pattern:
1. Create a new function
2. Add corresponding menu option
3. Call function when user selects that option

---

## Author Notes

This project is designed as a practical introduction to Python programming concepts. It emphasizes clean code, user experience, and practical problem-solving. The application can be extended significantly to include more advanced features like file handling, database integration, or graphical interfaces.

---

## Conclusion

The Shopping List Manager is an excellent beginner-to-intermediate Python project that reinforces fundamental programming concepts while creating a useful, practical application. Happy coding!

---

**Last Updated**: November 19, 2025
