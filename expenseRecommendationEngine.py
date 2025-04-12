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
"[0] = daily" \
"[1] = weekly" \
"[2] = monthly")

while True:
    period = input("period = ")