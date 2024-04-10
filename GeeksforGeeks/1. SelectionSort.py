class Solution: 
    def select(self, arr, i):
        # code here
        selectionSort(arr,i)
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            minIndex = i
            for j in range(i,len(arr),1):
                if arr[minIndex] > arr[j]:
                    minIndex = j
            arr[minIndex],arr[i] = arr[i],arr[minIndex]