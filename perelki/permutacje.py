def permute(nums: list[int]) -> list[list[int]]:
        answer = []
        part = []
        used = [False for i in range(len(nums))]
        def rek(i): #void, i - rek step
            nonlocal nums , answer , part , used
            if i >= len(nums): 
                answer.append(part.copy())
                # part.pop()
                return
            
            for idx in range(len(nums)):
                if used[idx]: continue
                part.append(nums[idx])
                used[idx] = True
                rek(i+1)
                part.pop()
                used[idx] = False
        rek(0)
        return answer

print(permute([1,2,3,4]))