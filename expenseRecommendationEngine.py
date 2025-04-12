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
def validate_index_input(name, input):
    while True:
        print(name, "= ")
        try:
            input = int(input)
            break
        except ValueError:
            print("Enter only the index numbers specified... (e.g 0,1,2 etc)")
    return input


#provide the period
print("Provide the time frame of your current expense (as):\n" \
"[0] = daily\n" \
"[1] = weekly\n" \
"[2] = monthly\n")

period = input("period = ")
period = validate_index_input("period", period)


        
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
    selectedCategory = input("Your Input: ")
    selectedCategory = validate_index_input("Category",selectedCategory)



get_daily_expense()