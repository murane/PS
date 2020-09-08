class Solution:
    def maxProfit(self, prices) -> int:
        lst=[]
        cur=0
        diff=0
        for i,num in enumerate(prices):
            if i==0:
                cur=num
                continue
            if cur>num:
                cur=num
                lst.append(diff)
            else:
                diff=max(diff,num-cur)
            if i==len(prices)-1:
                lst.append(diff)
        return max(lst)

if __name__ == '__main__':
    sol=Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))