import collections

def coin_change_helper(memo, coins, amount):
    # if the amount is in the memo, return the value for that amount
    if memo[amount]:
        return memo[amount]

    # if the amount == 0, there are 0 ways to make change
    if amount == 0:
        return 0

    # initialize number of ways for this amount to infinity
    memo[amount] = float("inf")

    # loop through the coins
    for coin in coins:
        # if the coin can be used
        if amount - coin >= 0:
            min_change_for_coin = coin_change_helper(memo, coins, amount - coin) + 1
            # set the memo for the amount by choosing the minimum value 
            # between what is currently stored in the memo for the amount 
            # and the recursive calculation of the amount of ways 
            # to make change if we were to use the coin
            memo[amount] = min(memo[amount], min_change_for_coin)

    # return the number of ways to make change for this amount
    return memo[amount]

def coin_change(amount, coins):
    # set up memo with defaultdict
    # defaultdict is purely a convenience. A regular dict would work with
    # appropriate code changes.
    memo = collections.defaultdict(int)
    # calculate result using helper
    result = coin_change_helper(memo, coins, amount)
    # return result if possible to make change, otherwise return -1
    return result if result != float("inf") else -1


### Test Case #1

amount = 11
coins = [5, 1, 2]

assert coin_change(amount, coins) == 3

### Test Case #2

amount = 3
coins = [2]

assert coin_change(amount, coins) == -1

### Test Case #3

amount = 0
coins = [1]

assert coin_change(amount, coins) == 0

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
