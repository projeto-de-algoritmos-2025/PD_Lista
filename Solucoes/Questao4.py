class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9 + 7  # Para evitar estouro de número, usamos módulo grande
        m = len(group)   # Número total de crimes

        # dp[i][j] = número de formas de atingir lucro j usando i membros
        # Inicializamos todos com 0, exceto dp[0][0] = 1 (caso base: sem crimes, lucro 0)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # Iteramos por cada crime
        for k in range(m):
            g = group[k]   # membros necessários para esse crime
            p = profit[k]  # lucro gerado por esse crime

            # Atualizamos a DP de forma reversa (de trás para frente)
            # para evitar sobrescrever estados ainda não processados
            for i in range(n, g - 1, -1):  # membros disponíveis (do maior para o necessário)
                for j in range(minProfit, -1, -1):  # lucro acumulado (do maior para o menor)
                    # Novo lucro: soma do atual com o lucro do crime, limitado a minProfit
                    new_profit = min(minProfit, j + p)
                    # Atualiza a quantidade de formas de atingir esse novo estado
                    dp[i][new_profit] = (dp[i][new_profit] + dp[i - g][j]) % MOD

        # Soma todas as formas válidas que atingem pelo menos minProfit com qualquer número de membros
        return sum(dp[i][minProfit] for i in range(n + 1)) % MOD
