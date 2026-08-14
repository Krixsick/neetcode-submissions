class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        -people -> array where people[i] weight of ith person
        -each boat can carry max 2 ppl
            ->each boat can carry weight <= limit
        -want to return minimum boats needed to carry everyone
        -we can sort first
            -
        """

        people.sort()
        boats = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            
            r -= 1
            boats += 1
        return boats
            

            

