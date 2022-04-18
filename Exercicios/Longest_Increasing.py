class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # inicializa todo o pd com 1
        pd = [1]*len(nums)

        # começamos a partir do segundo elemento, pois o primeiro ja descobrimos

        for i in range(1, len(nums)):

            # verifica j ate o i e atualiza o valor max

            for j in range(i):

                if nums[i] > nums[j]:
                    pd[i] = max(pd[j] + 1, pd[i])

        return max(pd)