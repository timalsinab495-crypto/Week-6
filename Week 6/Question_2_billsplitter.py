import random

random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750


def split_bill(friends, total):
    share = total / len(friends)
    return share


def pick_lucky(friends):
    lucky = random.choice(friends)
    return lucky


def final_summary(friends, total):
    share = split_bill(friends, total)
    lucky = pick_lucky(friends)

    print("---- Bill Split ----")
    for friend in friends:
        print(friend, "pays NPR", share)

    print()
    print("Lucky person:", lucky)

    # Local variable - only used inside this function
    lucky_total = share + 50
    print(lucky, "pays extra NPR 50, so total:", lucky_total)


final_summary(friends, total_bill)