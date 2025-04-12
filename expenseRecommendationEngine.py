from collections import defaultdict

categories = {
    "food" : defaultdict(list),
    "transport" : defaultdict(list),
    "books" : defaultdict(list),
    "bills" : defaultdict(list),
    "entertaiment" : defaultdict(list),
    "unavailable" : defaultdict(list)
}


#provide the period
print("Provide the time frame of your current expense (as):\n" \
"[0] = daily\n" \
"[1] = weekly\n" \
"[2] = monthly\n")

while True:
    period = input("period = ")
    try:
        period = int(period)
        break
    except ValueError:
        print("Enter only the numbers 0,1,2")

def display_options():
    print("\nThese are the available options for you to choose from. Use the index numbers 0,1,... to select an option.")
    index = 0
    for option in categories:
        if index == 5:
            break
        print("[", str(index), "] = ", option)
        index = index + 1

# def get_daily_expense():
#     expenseDict = {}

display_options()