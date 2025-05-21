# 853. Car Fleet

## Problem  
There are `n` cars going to the same destination along a one-lane road. The destination is `target` miles away.  
Each car `i` starts at `position[i]` and drives at constant speed `speed[i]`.  
A car can never pass another car ahead of it, but it can catch up and form a fleet.  
A **car fleet** is some non-empty set of cars that travel together at the same speed and position.

Return the number of car fleets that will arrive at the destination.

## Thought process  
We want to know how many groups of cars reach the target without merging into another.  
Since no car can overtake another, we process cars starting from the ones closest to the destination.  
If a car takes longer than the car ahead of it to reach the target, it can't catch up and will form its own fleet.  
Otherwise, it joins the fleet ahead.

## Approach  
- Pair each car's position and speed  
- Sort the cars by position in descending order (start from the closest to target)  
- For each car, compute the time it needs to reach the target  
- Use a stack to track fleet times  
  - If the current car takes more time than the car ahead, it can't catch up and starts a new fleet  
  - Else, it merges with the fleet ahead (don’t push to the stack)

## Complexity  
- Time: O(n log n)  
- Space: O(n)