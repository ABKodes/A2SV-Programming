class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        size = len(people)
        left = 0
        right = size - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats
