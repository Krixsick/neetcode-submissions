class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        weight_acc = r
        while l <= r:
            middle = (l + r) // 2
            acc = 0 
            days_counted = 1
            for index in range(len(weights)):
                if acc + weights[index] <= middle:
                    acc += weights[index]
                else:
                    days_counted += 1
                    acc = weights[index]
            if days_counted > days:
                l = middle + 1
            else:
                weight_acc = middle
                r = middle - 1

        return weight_acc