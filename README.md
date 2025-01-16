# Coins Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

Assume that there is an infinite number of each kind of coin.

For example, given a `coins` list of `[1, 2, 5]` and an `amount` of `11`, the function should return `3` because we can make `11` with `5`, `5`, and `1` coins. Notice that `5` is used twice. There are other ways to make `11`, but all require more coins.

## Examples

### Example 1

```py
amount = 11
coins = [1,2,5]
coin_change(amount, coins)
```

Produces

```py
3
```

### Example 2

```py
amount = 3
coins = [2]
coin_change(amount, coins)
```

Produces

```py
-1
```

### Example 3

```py
amount = 0
coins = [1]
coin_change(amount, coins)
```

Produces

```py
0
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I return if the coins array is empty?

A: Assume the coins array is not empty.

#### Q: How do I handle negative amounts?

A: Assume all amounts will be 0 or greater.

#### Q: What do I return if the coins cannot make up the amount?

A: Return -1 if you cannot make change with the coins provided.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper and a very small example like `amount = 3` and `coins = [1, 2]`. Encourage them not to jump right to the result of two coins (1 + 2 = 3) but to also think about how they look for other coin combinations (e.g. 1 + 1 + 1 = 3).

- Another hint is that this problem can be solved using recursion, then further optimized using dynamic programming. Encourage them to approach the problem recursively, then go back and refactor their solution with dynamic programming.

- Encourage them to take a look at the recursive calls being made. Remind them that creating a memo (dictionary) with the amount being a key and the value of that key being the number of coins to make change with that amount.

- Use of the `min` function can be used to determine the minimum value between two integers. For example, `min(5, 2)` will return the value 2. We can use the `min` function to consistently ensure the amount in the memo is the minimum amount of coins we can use.

- Remind them they can use collections.defaultdict to create the memo. This will eliminate the need to handle the case when adding to a dictionary and the key has not yet been explicitly added to the dictionary. (https://docs.python.org/3/library/collections.html#collections.defaultdict)

- If the interviewee does not want to attempt this problem using recursion or dynamic programming, that's totally ok! It can also be solved using iteration and keeping track of the biggest coin that can be subtracted from the amount until it reaches 0 or (in the event that change cannot be made from the provided coins) a negative amount. However, there are some coin values for which this approach will _not_ produce the correct result. For example, if the coins array is `[1, 15, 25]` and the amount is `30`, the correct answer is `2` (15 + 15), but the iterative approach will return `6` (25 + 1 + 1 + 1 + 1 + 1).

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What are the time/space complexities of the sample solution?

- If you wrote a recursive solution without dynamic programming, try incorporating dynamic programming into your approach.
