from collections import defaultdict

categories = {
    "food" : defaultdict(list),
    "transport" : defaultdict(list),
    "books" : defaultdict(list),
    "bills" : defaultdict(list),
    "entertaiment" : defaultdict(list),
    "unavailable" : defaultdict(list)
}

#validates the index selected by the user
def validate_index_input(name):
    while True:
        result = input(f"{name} = ")
        try:
            result = int(result)
            break
        except ValueError:
            try:
                result = float(result)
                break
            except ValueError:
                print("Enter only the index numbers specified... (e.g 0,1,2 etc)")
    return result


#provide the period
print("Provide the time frame of your current expense (as):\n" \
"[0] = daily\n" \
"[1] = weekly\n" \
"[2] = monthly\n")

period = validate_index_input("period")


        
#displays the available category to the user
def display_category():
    print("\nThese are the available category for you to choose from. Use the index numbers 0,1,... to select an option.")
    index = 0
    for option in categories:
        if index == 5:
            break
        print("[", str(index), "] = ", option)
        index = index + 1

#obtains the daily expenses (if selected)
def get_daily_expense():
    expenseDict = {}
    display_category() #display the available options
    selectedCategory = validate_index_input("Category")
    endRequest = validate_index_input("Enter [1] to proceed: ")
    while endRequest != 0 and endRequest == 1:
        amount = validate_index_input("Enter the expense amount: ")
        match selectedCategory:
            case 0:
                categories["food"]["food"].append(amount)
            case 1:
                categories["transport"]["transport"].append(amount)
            case 2:
                categories["books"]["books"].append(amount)
            case 3:
                categories["bills"]["bills"].append(amount)
            case 4:
                categories["entertaiment"]["entertaiment"].append(amount)
            case _:
                print("This category doesn't exists!!!")
        
        endRequest = validate_index_input("Enter [0] to terminate and [1] to proceed: ")
    continueProcess = validate_index_input("Would you like to continue the process? [0] for no, [1] for yes")
    if continueProcess:
        get_daily_expense()
        



get_daily_expense()

print(categories["food"])
print(categories["transport"])