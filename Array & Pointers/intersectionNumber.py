# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

def intersection(nums1,nums2):
    res=[]
    hm={}
    for num in nums1:
        hm[num]=hm.get(num,0)+1
    for num in nums2:
        if num in hm and hm[num]>0:
            res.append(num)
    print(res)

intersection([1,2,2],[2])
