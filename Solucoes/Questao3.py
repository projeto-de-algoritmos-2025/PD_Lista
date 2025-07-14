class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9 + 7

        # dp[m][p]: nº de esquemas usando m membros com lucro >= p (limitado a minProfit)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # 1 forma de ter 0 membros e 0 lucro

        for g, p in zip(group, profit):
            for m in range(n, g - 1, -1):
                for pr in range(minProfit, -1, -1):
                    new_pr = min(minProfit, pr + p)
                    dp[m][new_pr] = (dp[m][new_pr] + dp[m - g][pr]) % MOD

        # Soma todos os esquemas com lucro >= minProfit
        return sum(dp[m][minProfit] for m in range(n + 1)) % MOD
