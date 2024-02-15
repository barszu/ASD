from egzP4atesty import runtests 
"""
SOLUTION: 
- sort po poczatkach
- z krancowych -> Longest increasing subsequence
"""

def lengthOfLIS(nums: list[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        # dp[n-1] = 1

        for i in range(n-2,-1,-1):
            for k in range(i+1,n):
                if nums[i] <= nums[k]: #can be extended
                    dp[i] = max(dp[i] , dp[k]+1 )

        return max(dp)

    
def LIS(nums): #zachlan
    # kiedy nie da sie rozszerzyc okna napraw okno 
    # zamieniajac 1 wiekszy el od pivota ( nums[i] ) -> binsearch
    def binsearch(nums: list[int], target: int) -> int: # [3,5] t=4 -> 3
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (r+l)//2
            if nums[mid] == target: return mid
            elif target < nums[mid] :
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
        return l # [3,5] t=4 -> 5
    
    n = len(nums)
    lis = [nums[0]]
    for i in range(1,n):
        if nums[i] >= lis[-1]: lis.append(nums[i])
        else: lis[ binsearch(lis, nums[i]) ] = nums[i] #gdzie trzeba wkleic aby naprawic
    return lis
            

def mosty ( T ):
    #tutaj proszę wpisać własną implementację 
    T.sort()
    # q = lengthOfLIS([x[1] for x in T])
    q = len(LIS([x[1] for x in T]))
    return q

runtests ( mosty, all_tests=True )
# q = lengthOfLIS([2,3,5,4,6])
# print(q)