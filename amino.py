import bio

mass = input("Enter your value: ")
coins = input("Enter your value: ")
mass = int(mass)
coins = [int(c) for c in coins.split(',')]

print(mass, coins)

def calc_combinations(mass, coins):
    print("mass", mass, "coins", coins)
    if mass==0:
        return 1
    useful_coins = [coin for coin in coins if coin<=mass]
    if len(useful_coins)==0:
        print("mass", mass, "coins", coins, "0")
        return 0
    if len(useful_coins)==1:
        result = 1 if useful_coins[0]==mass else 0
        print("mass", mass, "coins", coins, result)
        return result
    result = sum([calc_combinations(mass-i, coins) for i in coins])
    print("mass", mass, "coins", coins, result)
    return result

result = calc_combinations(mass, coins)
print(result)