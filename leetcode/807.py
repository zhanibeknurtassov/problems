from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        sum = 0
        n = len(grid)
        hmax = [0]*n
        vmax = [0]*n
        for i in range(n):
            hmax[i] = grid[0][i]
            for j in range(n):
                if grid[j][i]>hmax[i]:
                    hmax[i] = grid[j][i]
        # print(hmax)   
        for i in range(n):
            vmax[i] = grid[i][0]
            for j in range(n):
                if grid[i][j]>vmax[i]:
                    vmax[i] = grid[i][j]
        # print(vmax)

        for i in range(n):
            for j in range(n):
                sum+=min(hmax[i], vmax[j])-grid[i][j]
        return sum


# --- Код для запуска ---
if __name__ == "__main__":
    # Тестовые данные (можете подставить любые свои значения)
    grid_test = [
        [3, 0, 8, 4],
        [2, 4, 5, 7],
        [9, 2, 6, 3],
        [0, 3, 1, 0]
    ]
    
    # Инициализация класса
    sol = Solution()
    
    # Вызов метода
    result = sol.maxIncreaseKeepingSkyline(grid_test)
    
    # Вывод возвращаемого значения (когда вы добавите return)
    print("Return:", result)