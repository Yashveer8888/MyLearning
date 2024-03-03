arr=[50,1,77,6,2,9,7,1,0]
def QuickSort(arr):
   if(len(arr)<=1):
      return arr
   pivot=arr[len(arr)-1]
   p=0
   for j in range(len(arr)-1):
      if(arr[j]<=pivot):
         arr[p],arr[j]=arr[j],arr[p]
         p+=1
   arr[p],arr[len(arr)-1]=arr[len(arr)-1],arr[p]
   less=arr[:p]
   greater=arr[p+1:]
   return QuickSort(less)+[pivot]+QuickSort(greater)
print(QuickSort(arr))


def QuickSort(arr):
   if len(arr)<=1:
      return arr
   pivot=arr[0]
   less=[x for x in arr[1:] if x<=pivot]
   greater=[x for x in arr[1:] if x>pivot]
   return QuickSort(less)+[pivot]+QuickSort(greater)
print(QuickSort(arr))
