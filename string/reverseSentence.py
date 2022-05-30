class Solution:
    def reverseWords(self, s: str) -> str:
        l, r = 0, len(s)-1
        
#         trim and redefine l and r boundaries
        while l <= r and s[l] ==" ":
            l+=1
        
        while l <= r and s[r] ==" ":
            r-=1
        
        queue, word = deque(), []
        
        while l <= r:
            if s[l] == " " and word:
                queue.appendleft(''.join(word))
                word=[]
            elif s[l] != " ":
                word.append(s[l])
            l+=1
        queue.appendleft(''.join(word))
        
        return ' '.join(queue)
