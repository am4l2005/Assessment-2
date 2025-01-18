menu = {
    11: {
        "Product": "Popcorn",
        "ID": 11,
        "Stock": 10,
        "Price": 4,
    },
    22: {
        "Product": "Chips",
        "ID": 22,
        "Stock": 10,
        "Price": 2,
    },
    33: {
        "Product": "Cookies",
        "ID": 33,
        "Stock": 10,
        "Price": 3,
    },
    44: {
        "Product": "Juice",
        "ID": 44,
        "Stock": 10,
        "Price": 2,
    },
    55: {
        "Product": "Soda",
        "ID": 55,
        "Stock": 10,
        "Price": 2,
    },
    66: {
        "Product": "Coffee",
        "ID": 66,
        "Stock": 10,
        "Price": 3,
    }
}

print("Welcome to our Vending Machine!\n")
print("Options:\n1 - List all items in the menu\n2 - List drinks only\n3 - List snacks only\n")
print("Follow the prompts to make your selection and purchase items.\n")

while True:
    newitem = 0
    userchoice = input("Please choose an option (1, 2, or 3): ")
    if userchoice in {"1", "2", "3"}:
        for Id, Menu in menu.items():
            if userchoice == "1" or (userchoice == "2" and Id > 33) or (userchoice == "3" and Id <= 33):
                print(f"Product -> {Menu['Product']}, ID -> {Menu['ID']}, Stock -> {Menu['Stock']}, Price -> ${Menu['Price']}")
    else:
        print("Error! Please type 1, 2 or 3!\n")
        continue

    try:
        userchoice = int(input("Enter the code of an item you want: "))
    except ValueError:
        print("Use numbers\n")
        continue

    if userchoice in menu:
        if menu[userchoice]["Stock"] == 0:
            print(f"Sorry! We're out of {menu[userchoice]['Product']}")
        else:
            if userchoice > 33:
                newitem = userchoice - 33
            else:
                newitem = userchoice + 33
            if menu[newitem]['Stock'] != 0:
                extra = input(f"Would you like to add {menu[newitem]['Product']} for ${menu[newitem]['Price']} (y/n) ")
                if extra == 'y':
                    total = menu[newitem]['Price'] + menu[userchoice]['Price']
                    print(f"Congrats! You will get {menu[userchoice]['Product']} & {menu[newitem]['Product']}")
                else:
                    total = menu[userchoice]['Price']
                    print(f"Congrats! You will get {menu[userchoice]['Product']}")
            else:
                total = menu[userchoice]['Price']
                print(f"Congrats! You will get {menu[userchoice]['Product']}")
        try:
            payment = int(input(f"Total price is ${total}!\nPlease enter numbers to pay: "))
        except ValueError:
            print("Use numbers")
            continue

        if payment < total:
            print("Purchase cancelled")
            continue
        else:
            payment = payment - total
            print(f"Your change is ${payment}")
            menu[userchoice]['Stock'] = menu[userchoice]['Stock'] - 1
            if newitem > 0:
                menu[newitem]['Stock'] = menu[newitem]['Stock'] - 1
            repeat = input("Wanna repeat the program? (y/n) ")
            if repeat == "y":
                continue
            else:
                print("Thank you and come again <3 !!")
                break
    else:
        print("Item is not listed")