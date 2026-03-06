class Solution:
    def selectionSort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            Min = arr[i]
            MinI = i

            for j in range(i + 1, n):
                if arr[j] < Min:
                    Min = arr[j]
                    MinI = j

            arr[i], arr[MinI] = arr[MinI], arr[i]

        return arr