class Solution:
    def canPartitionKSubsets(self, nums: 'List[int]', k: 'int') -> 'bool':
        # 如果数组只有一个元素，则直接返回true
        if k == 1:
            return True

        n = len(nums)
        if k > n:
            return False

        # 如果数组元素总和不能被k整除，则不会成功
        total = sum(nums)
        if total % k :
            return False

        target = total / k
        visit = [0] * n

        def dfs(k,ind,sum,cnt):
            if k== 1:
                return True
            if sum==target and cnt>0:
                return dfs(k-1,0,0,0)
            for i in range(ind,n):
                if not visit[i] and sum+nums[i]<=target:
                    visit[i]=1
                    if dfs(k,i+1,sum+nums[i],cnt+1): 
                        return True
                    visit[i]=0
            return False

        return dfs(k,0,0,0)