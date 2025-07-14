class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        # Inicializa a linha anterior com os valores base: distância de "" para word2
        prev = list(range(n + 1))  # prev[j] representa dp[i-1][j]
        curr = [0] * (n + 1)       # curr[j] representa dp[i][j]

        for i in range(1, m + 1):
            curr[0] = i  # Transformar os primeiros i caracteres de word1 em string vazia requer i deleções

            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Se os caracteres são iguais, nenhuma operação é necessária
                    curr[j] = prev[j - 1]
                else:
                    # Calcula o mínimo entre:
                    # - Inserção:    curr[j - 1] + 1
                    # - Remoção:     prev[j] + 1
                    # - Substituição:prev[j - 1] + 1
                    curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])

            # Troca as referências para a próxima iteração
            prev, curr = curr, prev

        return prev[n]  # Resultado final: transformar word1[:m] em word2[:n]
