class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """-n cars going same dir in 1 lane highway
        -position[i] position of ith car
        -speed[i] speed of ith car
        -destination at position target miles


        """
        cars = sorted(
            zip(position, speed),
            reverse=True
        )
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

