from typing import Dict, List, Callable, Tuple, TypeVar, Iterable, Optional
import os
import pickle

Item = Tuple[str, str]
ShoppingList = List[Item]
Operation = Callable[[ShoppingList], ShoppingList]

T = TypeVar('T')

def offer_options(options: Iterable[T]) -> Optional[T]:
    """
    Prompts user to choose from `options` and returns the choice, or `None`
    if the user cancelled
    """

    cancel_option = 'Cancel'
    options = list(options) + [cancel_option]
    keys = map(str, range(1, len(options) + 1))
    options = dict(zip(keys,options))

    while True:
        for num, name in options.items():
            print(num,":", name)
        inp = input("Choose a number: ")

        if inp in options.keys():
            choice = options[inp]
            return choice if choice != cancel_option else None

def get_item_choice(shopping_list: ShoppingList) -> ShoppingList:
    """gets the index of the item given, or returns -1 if not found"""

    item_name = offer_options([item[0] for item in shopping_list])

    if item_name is None:
        return None
    
    else:
        item_index = find_item_by_name(shopping_list, item_name)
        item = shopping_list[item_index]
        print('Chosen item:')
        display_item(item)
        return item_index
    
def get_item_name() -> str:
    """gets item from user"""

    return input('Enter the name of item: ')

def get_item_quantity() -> str:
    """gets item from user"""
    return input('Enter the item quantity: ')

def display_item(item: Item) -> None:
    """displays an item"""
    print('Name', item[0], 'Quantity', item[1])

def find_item_by_name(shopping_list: ShoppingList, item_name: str) -> int:
    """
    Return the index of the item with the given name, or -1 if not found.
    """
    for i, item in enumerate(shopping_list):
        if item[0] == item_name:
            return i

    return -1

def add_item(shopping_list: ShoppingList) -> ShoppingList:
    """
    Add an item specified by thge user to the shopping list
    """

    item_name = get_item_name()

    item_in_list = find_item_by_name(shopping_list, item_name) >= 0

    if item_in_list:
        print("Item already in list")
        return shopping_list

    quantity = get_item_quantity()
    new_item: Item = (item_name,quantity)
    
    return shopping_list + [new_item]

def view_items(shopping_list: ShoppingList) -> ShoppingList:
    """
    Displays the items in the shopping list
    """
    

    print(f'\nYou have {len(shopping_list)} item(s) in your shopping list:')
    for item in shopping_list:
        display_item(item)
    print()

    return shopping_list

def remove_item(shopping_list: ShoppingList) -> ShoppingList:
    """removes item from ShoppingList, and returns the ShoppingList"""

    item_index = get_item_choice(shopping_list)
    del shopping_list[item_index]

    return shopping_list

def edit_item(shopping_list: ShoppingList) -> ShoppingList:
    """
    edits the quantity or the name of the item
    """
    item_index = get_item_choice(shopping_list)
    item = shopping_list[item_index]

    def update_name():  
        return (get_item_name(),item[1])
    
    def update_quantity():
        return (item[0],get_item_quantity())

    options = {'Name': update_name, 'Quantity': update_quantity}
    choice = offer_options(options.keys())

    if choice is None:
        return shopping_list
    else:
        shopping_list[item_index] = options[choice]()
        return shopping_list
    
operations: Dict[str,Operation] = {
    "Add items": add_item,
    "View items": view_items,
    "Edit items": edit_item,
    "Remove items": remove_item
} 

if __name__ == "__main__":

    shopping_list_file = './shopping_list_data'
    
    shopping_list: ShoppingList = []

    if os.path.exists(shopping_list_file):
        with open(shopping_list_file,'rb') as f:
            shopping_list = pickle.load(f)

    while True:
        operation_key = offer_options(operations.keys())

        if operation_key is None:
            break

        shopping_list = operations[operation_key](shopping_list)

    with open(shopping_list_file,'wb') as f:
        pickle.dump(shopping_list,f)
