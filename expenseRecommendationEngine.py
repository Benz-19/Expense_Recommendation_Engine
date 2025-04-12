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
    except ValueError:
        print("Enter only the numbers 0,1,2")

