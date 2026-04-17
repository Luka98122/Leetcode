class Solution: #NA
    def threeSum(self, nums: list[int]) -> list[list[int]]:
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