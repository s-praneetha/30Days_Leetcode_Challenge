from random import randint
from bisect import bisect_right

class Solution:

    def __init__(self, w: List[int]):
        
        
        self.accumulation = w
        
        for i in range(1, len(w)):
            self.accumulation[i] = self.accumulation[i-1] + w[i]

            
            
    def pickIndex(self) -> int:
        
        sum_of_all_weight = self.accumulation[-1]
        
       
        random_value = randint(0, sum_of_all_weight-1)
        
        
        point = bisect_right(self.accumulation, random_value)
        
        return point