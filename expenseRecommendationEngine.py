from collections import defaultdict

categories = {
    "food" : defaultdict(list),
    "transport" : defaultdict(list),
    "books" : defaultdict(list),
    "bills" : defaultdict(list),
    "entertainment" : defaultdict(list),
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
def get_expense():
    display_category() #display the available options
    selectedCategory = validate_index_input("Category")
    endRequest = validate_index_input("Enter [1] to proceed: ")
    if endRequest not in [0,1]:
        print("Invalid input value, only [0] and [1] are allowed...")
        
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
                categories["entertainment"]["entertainment"].append(amount)
            case _:
                print("This category doesn't exists!!!")
        
        endRequest = validate_index_input("Enter [0] to terminate and [1] to proceed: ")
    continueProcess = validate_index_input("Would you like to continue the process? [0] for no, [1] for yes")
    if continueProcess:
        get_expense()
        
def process_sum_message(name):
    for items, value in categories.items():
        if items == name:
            if name in value:
                total = sum(value[name])
                print(f"Total of {name.capitalize()} sum = ", total)
            else:
                print(f"No values were found for {name.capitalize()}...")

def display_total_expense():
    #for food
    process_sum_message("food")
    #for transportation
    process_sum_message("transport")
    #for books
    process_sum_message("books")
    #for bills
    process_sum_message("bills")
    #for entertainment
    process_sum_message("entertainment")
    

get_expense()
display_total_expense()

