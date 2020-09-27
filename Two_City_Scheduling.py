class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        size = len(costs)/2
        CityA = 0
        CityB = 0
        costs=sorted(costs, key=lambda x:abs(x[0]-x[1]),reverse=True)
        for i in costs:
            if CityB<size and i[0] >= i[1]:
                res += i[1]
                CityB += 1
            elif CityA<size and i[1] >= i[0]:
                res += i[0]
                CityA += 1
            elif CityA == size:
                res += i[1]
            elif CityB == size:
                res += i[0]
        return res