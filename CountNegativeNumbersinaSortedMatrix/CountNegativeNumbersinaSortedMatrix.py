class Solution(object):
    def countNegatives(self, grid):
        tamanho_linha = len(grid[0])
        tamanho_coluna = len(grid)

        i = 0
        j = tamanho_linha -1

        totalNumbers = 0

        while i < tamanho_coluna and j >= 0:
            if grid[i][j] < 0:
                totalNumbers += tamanho_coluna -i
                j -= 1
            else:
                i += 1
        return totalNumbers
