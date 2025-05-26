# 875. Koko Eating Bananas

## Problem  
Koko loves to eat bananas. There are `n` piles of bananas, the `i-th` pile has `piles[i]` bananas. The guards have gone and will return in `h` hours. Koko can decide her eating speed `k` (bananas per hour). Each hour, she chooses a pile and eats `k` bananas from it. If the pile has less than `k` bananas, she eats all of it and won’t eat any more bananas during that hour.  
Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Thought process  
To minimize the eating speed `k`, I realized the problem has a monotonic nature: if Koko can finish eating at speed `k`, she can definitely finish at any speed higher than `k`. This suggests a binary search approach. We can binary search over the possible values of `k` from 1 to the maximum number of bananas in a pile.

## Approach  

- Set the binary search range from `1` to `max(piles)`
- For each middle value in the range:
  - Simulate the total hours Koko would take if she eats at that speed
  - Use `math.ceil(pile / k)` for each pile to compute hours
- If the total time is within `h`, store this `k` as a potential answer and search for a smaller `k`
- If it takes too long, increase `k` to speed up
- Return the smallest valid `k`

## Complexity  
- Time: O(n log m), where `n` is the number of piles and `m` is the max number of bananas in a pile  
- Space: O(1)