# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution(object):
    def getdistance(self, x, y):
        return math.sqrt(x ** 2 + y ** 2)

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minheap = []
        n = len(points)
        for i in range(n):
            x = points[i][0]
            y = points[i][1]
            heappush(minheap, (self.getdistance(x, y), points[i]))

        result = []
        for i in range(k):
            result.append((heappop(minheap)[1]))
        return result

