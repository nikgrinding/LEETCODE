# 121. Best Time to Buy and Sell Stock

## Problem  
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Thought process  
We need to find the lowest buying price and the highest possible selling price after that. As we iterate through the list, we keep track of the lowest price seen so far and calculate the potential profit at each step. If a better profit is found, we update our answer.

## Approach  

### Approach 1: Two pointers  
- Initialize two pointers, one for the buying day and one for the selling day
- Move the selling pointer forward and:
  - If the current selling price is greater than the buying price, calculate the profit
  - Else, update the buying pointer to the current selling day
- Keep track of the maximum profit seen so far

### Approach 2: Dynamic programming  
- Track the minimum price seen so far while iterating
- For each price, calculate the profit if we sell at that price using the lowest price so far
- Update the maximum profit accordingly

### Complexity comparison

| Approach   | Time     | Space |
|------------|----------|-------|
| Two pointer| O(n)     | O(1)  |
| Dynamic programming| O(n)     | O(1)  |