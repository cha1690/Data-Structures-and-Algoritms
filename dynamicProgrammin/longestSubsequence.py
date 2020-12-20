def lengthOfLIS(self, nums: List[int]) -> int:
    sub=[]
    for num in nums:
        len_sub=len(sub)
        pos=0
        while pos<=len_sub:
            if len_sub == pos:
                sub.append(num)
                break
            elif num <= sub[pos]:
                sub[pos] = num
                break
            else:
                pos+=1
    return len(sub)