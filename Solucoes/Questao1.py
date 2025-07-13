from bisect import bisect_right

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):

        # Passo 1: Combina os dados dos trabalhos em tuplas e ordena por endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # Lista com os horários de término (para busca binária)
        ends = [job[1] for job in jobs]
        
        # dp[i] = lucro máximo com os primeiros i trabalhos
        n = len(jobs)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]
            
            # Busca binária: índice do último trabalho que termina antes ou no início de s
            idx = bisect_right(ends, s)
            
            # Máximo entre não pegar o trabalho atual ou pegar e somar com dp[idx]
            dp[i] = max(dp[i - 1], p + dp[idx])
        
        return dp[n]

        