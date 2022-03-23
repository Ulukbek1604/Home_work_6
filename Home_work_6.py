class Solution:
    def binary_search(self, lst, target):
        low = 0
        high = len(lst) - 1
        search = False

        while low <= high and not search:
            middle = (low + high) // 2
            guess = lst[middle]
            if guess == target:
                search = True
            if guess > target:
                high = middle - 1
            else:
                low = middle + 1
        return search
