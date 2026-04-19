class Solution:
    def threeSum_orig(self, nums: list[int]) -> list[list[int]]: #NA
        nums.sort()
        # Original, very messy solution
        """
        Idea for solution:
        There are only a few valid types of answers:
        1. -a, -b, +c 
        2. -a, +b, +c
        3. -a, 0, +a
        
        We just have to do a two sum search for the first two types,
        which is worst case complexity O(n^2), where excactly half of nums
        are positive and half are negative. 
        
        Then we do a two pointer search to find equal positive and negative
        elements faster than O(n^2).        
        """
        
        neg = []
        pos = []
        zero_cnt = 0

        for num in nums:
            if num<0:
                neg.append(num)
            if num ==0:
                zero_cnt+=1
            if num>0:
                pos.append(num)
        
        neg = neg
        pos = pos
        
        a = [] #2 negatives + 1 positive triplets
        b = [] #1 negative + 2 positives triplets

        #2sum for neg
        d1 = {}
        for i,ne in enumerate(neg):
            if abs(ne) in d1.keys():
                d1[abs(ne)].append(i)
            else:
                d1[abs(ne)]=[i]
        
        for po in list(set(pos)):
            s1 = set()        
            for i,num in enumerate(neg):
                if po-abs(num) in d1.keys():
                    if i!=d1[po-abs(num)][-1]:
                        if not num in s1 and not (-abs(po-abs(num))) in s1:
                            a.append([num,-abs(po-abs(num)),po])
                            s1.add(num)
                            s1.add(-abs(po-abs(num)))
                              
        #2sum for pos     
        d2 = {}
        for i,po in enumerate(pos):
            if po in d2.keys():
                d2[po].append(i)
            else:
                d2[po]=[i]
        
        for ne in list(set(neg)):
            s1 = set()

            for i,num in enumerate(pos):
                if abs(ne)-num in d2.keys():
                    if i!=d2[abs(ne)-num][-1]:
                        if not num in s1 and not (abs(ne)-num) in s1:
                            b.append([num,abs(ne)-num,ne])
                            s1.add(num)
                            s1.add(abs(ne)-num)
        
        # Finding equal pos - neg pairs using two-pointer.
        # Looking back, could have been done with sets.
        p = 0
        res = []
        neg = list(set(neg))
        pos = list(set(pos))
        pos.sort()
        neg.sort()
        n = len(neg)-1
        if zero_cnt>0:
            while True:
                if n<0 or p>=len(pos): break

                if pos[p]==abs(neg[n]):
                    res.append([neg[n],0,pos[p]])
                    if p<len(pos)-1:
                        p+=1
                    else:
                        n-=1    
                else:
                    if abs(neg[n])>pos[p]:
                        p+=1
                        continue
                    else:
                        n-=1
                        continue
        if zero_cnt>=3:
            res.append([0,0,0])
        res = res + a + b
        return res
    def threeSum_old(self, nums: list[int]) -> list[list[int]]: #A
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
    def threeSum(self, nums: list[int]) -> list[list[int]]: #NA
        res = []
        nums.sort()
        for i,num in enumerate(nums):
            l = i+1
            r = len(nums)-1
            if i!=0 and num==nums[i-1]: continue
            while l<r:
                if num+nums[l]+nums[r]==0:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1

                    while l<r:
                        if nums[l]==nums[l-1]:
                            l+=1
                            continue
                        elif nums[r]==nums[r+1]:
                            r-=1
                            continue
                        else:
                            break
                    
                else:
                    if num+nums[l]+nums[r]>0:
                        r-=1
                    else:
                        l+=1
        return res