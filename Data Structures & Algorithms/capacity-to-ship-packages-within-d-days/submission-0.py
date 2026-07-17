class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minimum = max(weights)
        maximum = sum(weights)
        res = 0
        while minimum < maximum:
            middle =(minimum + maximum) // 2
            days_used = 1
            current_load = 0
            for index in range(len(weights)):
                if current_load + weights[index] <= middle:
                    current_load += weights[index]
                else:
                    days_used += 1
                    current_load = weights[index]
            if days_used <= days:
                maximum = middle
            else:
                minimum = middle + 1
        return minimum