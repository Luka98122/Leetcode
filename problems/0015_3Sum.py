class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res: set[tuple[int, int, int]] = set()

        n: list[int] = []
        p: list[int] = []
        z: list[int] = []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        N: set[int] = set(n)
        P: set[int] = set(p)

        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))

        if len(z) >= 3:
            res.add((0, 0, 0))

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -(n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted((n[i], n[j], target))))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -(p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted((p[i], p[j], target))))

        return [list(triplet) for triplet in res]


c = Solution()
c.threeSum([-1,0,1,2,-1,-4])
                