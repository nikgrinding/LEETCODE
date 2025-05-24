# 42. Trapping Rain Water

## Problem  
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Thought process  
To trap water at a position, we need to know the maximum height to the left and right. The water trapped is the minimum of those two minus the current height. To optimize space, I used two pointers moving inward, maintaining running max heights from both ends and adding trapped water accordingly.

## Approach  

- Initialize two pointers at both ends of the array
- Maintain `l_max` and `r_max` to track the highest walls seen from the left and right
- At each step:
  - Move the pointer on the shorter side inward
  - Update the corresponding max
  - Calculate trapped water using: `max_so_far - current_height`
- Add the trapped water to the total

## Complexity  
- Time: O(n)  
- Space: O(1)