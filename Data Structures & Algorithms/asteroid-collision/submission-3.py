class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        -you have a list of asteroids
            -indices of asteroid represents an asteroid
                -the absolute value is the size
                -the sign is the direction (pos -> right, neg -> left)
                -each asteroid moves at the same speed
                    -if two asteroids meet, the smaller one will explode
                    -if both are same size, both explodes
                    -otherwise if they are going in the same direction, they will never meet
        """
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                last_item = stack.pop()
                if -asteroid > last_item:
                    continue
                elif -asteroid < last_item:
                    stack.append(last_item)
                    break
                break
            else:
                stack.append(asteroid)
        return stack