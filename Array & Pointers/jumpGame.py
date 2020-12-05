class Solution:
    def jumpGame(self, nums):
        maxStep=0
        for index,num in enumerate(nums):
            if maxStep > index:
                return False
            maxStep = max(maxStep,index+num)
        return True