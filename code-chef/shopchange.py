def calculate_money(T):
    for i in range(T):
        cost = int(input())
        money_saved = 100 - cost
        print(money_saved)

T = int(input())
calculate_money(T)

